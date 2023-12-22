from litellm import completion
from trulens_eval.tru_custom_app import instrument

class RAG_openai:

    def __init__(self, vectordb):
        self.vectordb = vectordb


    @instrument
    def retrieve(self, query: str) -> list:
        """
        Retrieve relevant text from vector store.
        """
        retriever = self.vectordb.as_retriever()
        results = retriever.get_relevant_documents(query) 
        return results[0]  

    
    @instrument
    def generate_completion(self, query:str, context_str: list) -> str:
        """
        Generate answer from context.
        """
        messages = [{
            "role": "user",
            "content": 
                f"We have provided context information below. \n"
                f"---------------------\n"
                f"{context_str}"
                f"\n---------------------\n"
                f"Given this information, please answer the question: {query}"
        }]
        response = completion(model="gpt-3.5-turbo", messages=messages)
        response_txt = response.choices[0].message.content

        return response_txt
        

    @instrument
    def query(self, query:str ) -> str:
        context_str = self.retrieve(query)
        return self.generate_completion(query, context_str)