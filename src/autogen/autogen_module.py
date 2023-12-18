import os
from typing import List, Dict, Any
from pathlib import Path
from semantic_kernel.semantic_kernel_module import SemanticKernelModule
from taskweaver.taskweaver_module import TaskweaverModule
from agent_builder import AgentBuilder
from autogen.agentchat.contrib.retrieve_assistant_agent import RetrieveAssistantAgent
from autogen.agentchat.contrib.retrieve_user_proxy_agent import RetrieveUserProxyAgent
from autogen import AssistantAgent, UserProxyAgent, config_list_from_json
from llama_hub.file.unstructured import UnstructuredReader
from llama_index import download_loader, SimpleDirectoryReader, VectorStoreIndex, ServiceContext
from llama_index.vector_stores import ChromaVectorStore
from llama_index.storage.storage_context import StorageContext
from llama_index.embeddings import HuggingFaceEmbedding
from llama_index.node_parser import SimpleNodeParser
import chromadb

# Set up the environment variables
os.environ['OPENAI_API_KEY'] = 'Your key here'  # Replace with your actual API key

# Load data/documents
UnstructuredReader = download_loader('UnstructuredReader')
dir_reader = SimpleDirectoryReader(r"path to your folder", file_extractor={
    ".pdf": UnstructuredReader(),
    ".html": UnstructuredReader(),
    ".eml": UnstructuredReader(),
    ".xlsx": UnstructuredReader()
}, recursive=True)

documents = dir_reader.load_data()

# Create vector store/embeddings
db = chromadb.PersistentClient(path=r"path to your database")
chroma_client = chromadb.EphemeralClient()
chroma_collection = chroma_client.create_collection("collection_name")
embed_model = HuggingFaceEmbedding(model_name="BAAI/bge-base-en-v1.5") #TruEra Evaluation

# Extracting metadata and creating nodes
text_splitter = TokenTextSplitter(separator=" ", chunk_size=1024, chunk_overlap=128)
metadata_extractor = MetadataExtractor(extractors=[TitleExtractor(nodes=5), QuestionsAnsweredExtractor(questions=3)])
node_parser = SimpleNodeParser.from_defaults(text_splitter=text_splitter)

# Set up ChromaVectorStore and load in data
vector_store = ChromaVectorStore(chroma_collection=chroma_collection)
storage_context = StorageContext.from_defaults(vector_store=vector_store)
service_context = ServiceContext.from_defaults(embed_model=embed_model, node_parser=node_parser)
index = VectorStoreIndex.from_documents(documents, storage_context=storage_context, service_context=service_context)

# Custom context retrieval function
def query_vector_db(query_texts: List[str], n_results: int = 10, search_string: str = "", **kwargs) -> Dict[str, List[List[Any]]]:
    result_dict = {"ids": [], "documents": []}
    # Custom query logic goes here...
    return result_dict

class MyRetrieveUserProxyAgent(RetrieveUserProxyAgent):
    def query_vector_db(self, query_texts: List[str], n_results: int = 10, search_string: str = "", **kwargs) -> Dict[str, List[List[Any]]]:
        return query_vector_db(query_texts, n_results, search_string, **kwargs)

    def retrieve_docs(self, problem: str, n_results: int = 20, search_string: str = "", **kwargs):
        results = self.query_vector_db(query_texts=[problem], n_results=n_results, search_string=search_string, **kwargs)
        self._results = results
        print("doc_ids: ", results["ids"])

class AutoGenModule:
    """
    AutoGenModule with integrated Semantic Kernel and llama index.
    """
    ASSISTANT_PERSONA = (
        f"Only use provided functions. Do not ask the user for other actions. "
        f"Use functions to find unavailable information. "
        f"Today's date: {datetime.date.today().strftime('%B %d, %Y')}. "
        f"Reply TERMINATE when the task is done."
    )

    def __init__(self):
        self.kernel = kernel
        self.llm_config = llm_config or {}
        self.builder_config_path = builder_config_path
        self.builder = self.create_builder()
        self.semantic_kernel = SemanticKernelModule()
        self.taskweaver = TaskweaverModule()
        self.agent_builder = AgentBuilder()
        self.vector_index = index  # Integrated VectorStoreIndex
    
    def create_builder(self) -> AgentBuilder:
        """
        Create an instance of AgentBuilder.
        """
        if not self.builder_config_path:
            raise ValueError("Builder config path is required to create AgentBuilder.")
        return AgentBuilder(config_path=self.builder_config_path)

    def generate_response(self, user_input: str):
        # Use Semantic Kernel to interpret input and generate a response
        response = self.semantic_kernel.process_input(user_input)
        # Auto-generate content or code snippet based on the response
        generated_content = self.auto_generate(response)
        return generated_content

    def auto_generate(self, response: str):
        # Logic to generate content or code snippet
        # This can be customized based on project needs
        return f"Generated Content based on: {response}"
    
    def create_gemini_multimodal_agent(self):
        image_agent = MultimodalConversableAgent(
            "Gemini Vision",
            llm_config={"config_list": self.config_list_gemini_vision, "seed": 42},
            max_consecutive_auto_reply=1
        )

        user_proxy = UserProxyAgent(
            "user_proxy",
            human_input_mode="NEVER",
            max_consecutive_auto_reply=0
        )
        return image_agent, user_proxy
    
    def execute_code(self, code_snippet):
        """
        Execute a Python code snippet and return the result.
        Args:
            code (str): The Python code to execute.
        Returns:
            str: The output of the executed code.
        """
        # Here, we'll need to use the actual implementation for code execution.
        # This can be done through the TaskweaverModule or another execution environment.
        # The following is a placeholder for the actual implementation.
        try:
            execution_result = self.taskweaver.execute_code(code_snippet)
            return execution_result
        except Exception as e:
            return f"Error executing code: {str(e)}"
    
    def create_assistant_agent(self, name: str) -> AssistantAgent:
        # Create an AssistantAgent with the given name and persona
        return RetrieveAssistantAgent(name=name, system_message=self.ASSISTANT_PERSONA, llm_config=self.llm_config)

    def create_user_proxy_agent(self, name: str, max_auto_reply: Optional[int] = None, human_input: Optional[str] = "ALWAYS") -> UserProxyAgent:
        # Create a UserProxyAgent with the given name, max_auto_reply, and human_input mode
        return RetrieveUserProxyAgent(name=name, max_consecutive_auto_reply=max_auto_reply, human_input_mode=human_input)

    def query_vector_db(self, query_texts: List[str], n_results: int = 10, search_string: str = "", **kwargs):
        return query_vector_db(query_texts, n_results, search_string, **kwargs)
