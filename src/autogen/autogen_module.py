import os
from typing import List, Dict, Any, Optional
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
import json
import memgpt
import memgpt.autogen.memgpt_agent
from memgpt.autogen.memgpt_agent import create_memgpt_autogen_agent_from_config
class MemGPTMemoryManager:
    def __init__(self, storage_path: str):
        self.storage_path = Path(storage_path)
        self.storage_path.mkdir(parents=True, exist_ok=True)

    def save_memory(self, agent_name: str, memory_state: Dict):
        """Saves the memory state of a specific agent."""
        try:
            with open(self.storage_path / f"{agent_name}_memory.json", "w") as file:
                json.dump(memory_state, file)
        except Exception as e:
            print(f"Error saving memory state for agent {agent_name}: {e}")

    def load_memory(self, agent_name: str) -> Optional[Dict]:
        """Loads the memory state of a specific agent."""
        memory_file = self.storage_path / f"{agent_name}_memory.json"
        if memory_file.exists():
            try:
                with open(memory_file, "r") as file:
                    return json.load(file)
            except Exception as e:
                print(f"Error loading memory state for agent {agent_name}: {e}")
        return None

    def clear_memory(self, agent_name: str):
        """Clears the memory state of a specific agent."""
        memory_file = self.storage_path / f"{agent_name}_memory.json"
        if memory_file.exists():
            try:
                memory_file.unlink()
            except Exception as e:
                print(f"Error clearing memory state for agent {agent_name}: {e}")
class MemGPTAgent(ConversableAgent):
    def __init__(self, name: str, agent: _Agent, memory_manager: MemGPTMemoryManager, skip_verify=False):
        super().__init__(name)
        self.agent = agent
        self.memory_manager = memory_manager

    def save_memory_state(self):
        memory_state = self.agent.extract_memory_state()  # Assuming this method exists in the _Agent class
        self.memory_manager.save_memory(self.name, memory_state)

    def load_memory_state(self):
        memory_state = self.memory_manager.load_memory(self.name)
        if memory_state is not None:
            self.agent.set_memory_state(memory_state)  # Assuming this method exists in the _Agent class

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

    def __init__(self, memgpt_memory_path: str, openai_api_key: str): # needs to be more clear
        self.kernel = kernel
        self.llm_config = llm_config or {}
        self.builder_config_path = builder_config_path
        self.builder = self.create_builder()
        self.semantic_kernel = SemanticKernelModule()
        self.taskweaver = TaskweaverModule()
        self.agent_builder = AgentBuilder()
        self.vector_index = index  # Integrated VectorStoreIndex
        self.memgpt_memory_manager = MemGPTMemoryManager(memgpt_memory_path)
        # Set the environment variable for OpenAI API key
        os.environ['OPENAI_API_KEY'] = openai_api_key
        # MemGPT Configuration
        self.memgpt_config = {
            "model": "gpt-4",
            "preset": "memgpt_chat",
            "model_endpoint_type": "openai",
            "model_endpoint": "https://api.openai.com/v1",
            "context_window": 8192,
        }
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
    
    def auto_generate(self, response):
        return f"Generated Content based on: {response}"

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
 
    def create_memgpt_agent(self, agent_name: str):
        """
        Create and initialize a MemGPT agent.
        """
        memgpt_llm_config = {"config_list": [self.memgpt_config], "seed": 42}
        interface_kwargs = {
            "debug": False,
            "show_inner_thoughts": True,
            "show_function_outputs": False,
        }
        memgpt_agent = create_memgpt_autogen_agent_from_config(
            agent_name,
            llm_config=memgpt_llm_config,
            system_message=self.ASSISTANT_PERSONA,
            interface_kwargs=interface_kwargs,
            default_auto_reply="...",
            skip_verify=True,
        )
        memgpt_agent.memory_manager = self.memgpt_memory_manager
        return memgpt_agent
   
    def create_assistant_agent(self, name: str) -> AssistantAgent:
        # Create an AssistantAgent with the given name and persona
        return RetrieveAssistantAgent(name=name, system_message=self.ASSISTANT_PERSONA, llm_config=self.llm_config)

    def create_user_proxy_agent(self, name: str, max_auto_reply: Optional[int] = None, human_input: Optional[str] = "ALWAYS") -> UserProxyAgent:
        # Create a UserProxyAgent with the given name, max_auto_reply, and human_input mode
        return RetrieveUserProxyAgent(name=name, max_consecutive_auto_reply=max_auto_reply, human_input_mode=human_input)

    def query_vector_db(self, query_texts: List[str], n_results: int = 10, search_string: str = "", **kwargs):
        return query_vector_db(query_texts, n_results, search_string, **kwargs)
