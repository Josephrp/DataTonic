import chromadb
import google.generativeai as genai
import numpy as np
import openai
import os

from chromadb.utils import embedding_functions
from dotenv import load_dotenv

from langchain.document_loaders import TextLoader, DirectoryLoader
from langchain.text_splitter import RecursiveCharacterTextSplitter

from trulens_eval import Feedback, Select, Tru, TruCustomApp
from trulens_eval.feedback import Groundedness
from trulens_eval.feedback.provider.openai import OpenAI as fOpenAI
from trulens_eval.tru_custom_app import instrument


def parse_input(local_path: str) -> tuple:
    if not os.path.exists(local_path):
        os.mkdir(local_path)

    loader = DirectoryLoader(
        local_path,
        loader_cls=TextLoader,
        show_progress=True
    )
    documents = loader.load()

    text_splitter = RecursiveCharacterTextSplitter(
        chunk_size=1000,
        chunk_overlap=200
    )
    texts = text_splitter.split_documents(documents)
    
    id_list = [
        f'doc-{str(i).zfill(len(texts))}' for i, doc in enumerate(texts)
    ]
    text_content_list = [
        doc.page_content for doc in texts
    ]
    metadata_list = [
        doc.metadata for doc in texts
    ]

    return id_list, text_content_list, metadata_list


def get_embedding_functions():
    return {
        'gemini' : embedding_functions.GoogleGenerativeAiEmbeddingFunction(
            api_key=os.getenv("GOOGLE_API_KEY")
        ),
        'openai' : embedding_functions.OpenAIEmbeddingFunction(
            api_key=os.getenv("OPENAI_API_KEY"),
            model_name="text-embedding-ada-002"
        ),
        # 'jinaai' : embedding_functions.JinaEmbeddingFunction(
        #     api_key=os.getenv("JINAAI_API_KEY"),
        #     model_name="jina-embeddings-v2-base-en"
        # ),
        # 'cohere' : embedding_functions.CohereEmbeddingFunction(
        #     api_key=os.getenv('COHERE_API_KEY'),
        #     model_name="command-nightly"
        # )
        # TODO Hugging face, sentence transformer
    }


class RAG:

    def __init__(self, vector_store, provider: str):
        self.vector_store = vector_store
        self.provider = provider


    @instrument
    def retrieve(self, query: str) -> list:
        """
        Retrieve relevant text from vector store.
        """
        results = self.vector_store.query(
            query_texts=query,
            n_results=1
        )
        return results['documents'][0]

    
    @instrument
    def generate_completion(self, query:str, context_str: list) -> str:
        """
        Generate answer from context.
        """
        if self.provider == "gemini":
            message = [
                {
                    "role": "user",
                    "parts": [
                        f"We have provided context information below. \n"
                        f"---------------------\n"
                        f"{context_str}"
                        f"\n---------------------\n"
                        f"Given this information, please answer the question: {query}"
                    ]
                }
            ]
            genai.configure(
                api_key=os.getenv("GOOGLE_API_KEY")
            )
            model = genai.GenerativeModel('gemini-pro')
            response = model.generate_content(message)
            response_txt = response.text
            return response_txt

        elif self.provider == "openai":
            openai.api_key = os.getenv("OPENAI_API_KEY")
            completion = openai.chat.completions.create(
                model="gpt-3.5-turbo",
                temperature=0,
                messages=
                    [
                        {
                            "role" : "user",
                            "content": 
                                f"We have provided context information below. \n"
                                f"---------------------\n"
                                f"{context_str}"
                                f"\n---------------------\n"
                                f"Given this information, please answer the question: {query}"
                        }
                    ]
                ).choices[0].message.content
            return completion
        
        # TODO Hugging face, cohere, sentence transformer
        

    @instrument
    def query(self, query:str ) -> str:
        context_str = self.retrieve(query)
        completion = self.generate_completion(query, context_str)
        return completion


def get_feedbacks_for_openai() -> list:
    # Initialize provider class
    fopenai = fOpenAI()

    grounded = Groundedness(groundedness_provider=fopenai)

    # Define a groundedness feedback function
    f_groundedness = (
        Feedback(grounded.groundedness_measure_with_cot_reasons, name = "Groundedness")
        .on(Select.RecordCalls.retrieve.rets.collect())
        .on_output()
        .aggregate(grounded.grounded_statements_aggregator)
    )

    # Question/answer relevance between overall question and answer.
    f_qa_relevance = (
        Feedback(fopenai.relevance_with_cot_reasons, name = "Answer Relevance")
        .on(Select.RecordCalls.retrieve.args.query)
        .on_output()
    )

    # Question/statement relevance between question and each context chunk.
    f_context_relevance = (
        Feedback(fopenai.qs_relevance_with_cot_reasons, name = "Context Relevance")
        .on(Select.RecordCalls.retrieve.args.query)
        .on(Select.RecordCalls.retrieve.rets.collect())
        .aggregate(np.mean)
    )

    return [f_groundedness, f_qa_relevance, f_context_relevance]


def query_rag(rag):
    tru_rag = TruCustomApp(
        rag,
        app_id = provider,
        feedbacks = get_feedbacks_for_openai()
    )

    with tru_rag as _:
        rag.query("What is the news about Pando")


if __name__ == "__main__":
    load_dotenv('../../.env')

    id_list, text_content_list, metadata_list = parse_input('new-articles')
    chroma_client = chromadb.Client()

    embedding_functions_dict = get_embedding_functions()
    providers = embedding_functions_dict.keys()

    for provider in providers:
        print(f'Processing {provider = }')
        vector_store = chroma_client.get_or_create_collection(
            name=provider,
            embedding_function=embedding_functions_dict[provider]
        )
        vector_store.add(
            ids=id_list,
            documents=text_content_list,
            metadatas=metadata_list
        )
        print(f'Setup vector_store for {provider = }')
        query_rag(
            RAG(
                vector_store,   
                provider
            )
        )
        print(f'Finished query_rag for {provider = }')


    print('Launching Tru leaderboard')
    tru = Tru()
    tru.get_leaderboard(
        app_ids=providers
    )
    tru.run_dashboard()