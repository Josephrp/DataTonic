import textwrap
import os
import google.generativeai as genai
import numpy as np
# import streamlit as st

from dotenv import load_dotenv
from IPython.display import Markdown

from langchain_google_genai import ChatGoogleGenerativeAI
from langchain_google_genai import GoogleGenerativeAIEmbeddings

from langchain.document_loaders import TextLoader
from langchain.vectorstores import Chroma
from langchain.text_splitter import RecursiveCharacterTextSplitter
from langchain.document_loaders import DirectoryLoader

from trulens_eval import Feedback, Select, Tru, TruCustomApp
from trulens_eval.feedback import Groundedness
from trulens_eval.feedback.provider.openai import OpenAI as fOpenAI
from trulens_eval.tru_custom_app import instrument


def to_markdown(text):
  text = text.replace('•', '  *')
  return Markdown(textwrap.indent(text, '> ', predicate=lambda _: True))

load_dotenv()
GOOGLE_API_KEY= os.getenv("GOOGLE_API_KEY")

genai.configure(api_key=GOOGLE_API_KEY)
model = genai.GenerativeModel('gemini-pro')

if not os.path.exists('new-articles'):
    os.mkdir('new-articles')

loader = DirectoryLoader('./new-articles/', loader_cls=TextLoader, show_progress=True)
documents = loader.load()

text_splitter = RecursiveCharacterTextSplitter(chunk_size=1000, chunk_overlap=200)
texts = text_splitter.split_documents(documents)

embeddings = GoogleGenerativeAIEmbeddings(model="models/embedding-001")
vectordb = Chroma.from_documents(documents=texts, embedding=embeddings)

tru = Tru()

class RAG_from_scratch:
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
        model = genai.GenerativeModel('gemini-pro')
        response = model.generate_content(message)
        response_txt = response.text
        return response_txt
        

    @instrument
    def query(self, query:str ) -> str:
        context_str = self.retrieve(query)
        completion = self.generate_completion(query, context_str)
        return completion
    
rag = RAG_from_scratch()

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

tru_rag = TruCustomApp(
    rag,
    app_id = 'RAG v1',
    feedbacks = [f_groundedness, f_qa_relevance, f_context_relevance]
)

with tru_rag as recording:
    rag.query("What is the news about Pando")

tru.get_leaderboard(app_ids=["RAG v1"])

tru.run_dashboard()
