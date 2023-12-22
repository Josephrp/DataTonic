import os
import google.generativeai as genai
import numpy as np

from dotenv import load_dotenv

from langchain_google_genai import GoogleGenerativeAIEmbeddings

from langchain.document_loaders import TextLoader
from langchain.vectorstores import Chroma
from langchain.text_splitter import RecursiveCharacterTextSplitter
from langchain.document_loaders import DirectoryLoader

from trulens_eval import Feedback, Select, Tru, TruCustomApp
from trulens_eval.feedback import Groundedness
from trulens_eval.feedback.provider.openai import OpenAI as fOpenAI
from trulens_eval.tru_custom_app import instrument


def load_text(local_path: str) -> list:
    if not os.path.exists(local_path):
        os.mkdir(local_path)

    loader = DirectoryLoader(local_path, loader_cls=TextLoader, show_progress=True)
    documents = loader.load()

    text_splitter = RecursiveCharacterTextSplitter(chunk_size=1000, chunk_overlap=200)
    texts = text_splitter.split_documents(documents)
    
    return texts


class RAG_gemini:
    @instrument
    def retrieve(self, query: str) -> list:
        """
        Retrieve relevant text from vector store.
        """
        retriever = vectordb.as_retriever()
        results = retriever.get_relevant_documents(query) 
        return results[0]  

    
    @instrument
    def generate_completion(self, query:str, context_str: list) -> str:
        """
        Generate answer from context.
        """
        message = [{
            "role": "user",
            "parts": [
                f"We have provided context information below. \n"
                f"---------------------\n"
                f"{context_str}"
                f"\n---------------------\n"
                f"Given this information, please answer the question: {query}"
            ]
        }]
        GOOGLE_API_KEY = os.getenv("GOOGLE_API_KEY")
        genai.configure(api_key=GOOGLE_API_KEY)
        model = genai.GenerativeModel('gemini-pro')
        response = model.generate_content(message)
        response_txt = response.text
        return response_txt
        

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


def evaluate(app_id: str, rag, feedbacks: list):
    tru_rag = TruCustomApp(
        rag,
        app_id = app_id,
        feedbacks = feedbacks
    )

    with tru_rag as _:
        rag.query("What is the news about Pando")



if __name__ == "__main__":
    load_dotenv('../../.env')
    providers = {
        'openai' : {
            'rag': RAG_gemini(),
            'feedbacks': get_feedbacks_for_openai()
        },
    }

    texts = load_text('new-articles')

    embeddings = GoogleGenerativeAIEmbeddings(model="models/embedding-001")
    vectordb = Chroma.from_documents(documents=texts, embedding=embeddings)

    for app_id in providers:
        evaluate(
            app_id,
            providers[app_id]['rag'],
            providers[app_id]['feedbacks']
        )

    tru = Tru()
    tru.get_leaderboard(app_ids=['openai'])
    tru.run_dashboard()