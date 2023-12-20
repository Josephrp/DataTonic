import json
import asyncio
from dotenv import load_dotenv
from datetime import datetime
from autogen.autogen_module import AutoGenModule
from semantic_kernel.semantic_kernel_module import SemanticKernelModule
from taskweaver.taskweaver_module import TaskweaverModule
from agent_builder import AgentBuilder
from autogen.agentchat.contrib.retrieve_assistant_agent import RetrieveAssistantAgent
from autogen.agentchat.contrib.retrieve_user_proxy_agent import RetrieveUserProxyAgent

async def main():
    # Load environment variables from .env file
    load_dotenv()

    # Load the configuration list for different LLMs
    with open('OAI_CONFIG_LIST.json', 'r') as file:
        OAI_CONFIG_LIST = json.load(file)

    # Extract Gemini configurations from the list
    config_list_gemini = [config for config in OAI_CONFIG_LIST if 'gemini' in config["model"]]
    config_list_gemini_vision = [config for config in OAI_CONFIG_LIST if 'gemini-pro-vision' in config["model"]]

    # Initialize the AutoGenModule with the Semantic Kernel and Taskweaver modules
    semantic_kernel = SemanticKernelModule()
    taskweaver = TaskweaverModule()
    agent_builder = AgentBuilder()

    autogen_module = AutoGenModule()
    autogen_module.semantic_kernel = semantic_kernel
    autogen_module.taskweaver = taskweaver
    autogen_module.agent_builder = agent_builder

    # Create Gemini RAG and Multimodal Agents
    assistant = autogen_module.create_assistant_agent(name="Assistant")
    user_proxy = autogen_module.create_user_proxy_agent(name="User_Proxy", max_auto_reply=3)
    image_agent, _ = autogen_module.create_gemini_multimodal_agent()

    # Get user input to trigger the UserProxyAgent and start the interaction
    user_input = input("Please provide a description for the task you'd like to perform: ")

    # Use the user input to start the UserProxyAgent
    await user_proxy.initiate_chat(assistant, message=user_input)

    # Process the interaction based on the task description
    task_description = user_input
    agent_list, agent_configs = autogen_module.build_agents_for_task(task_description)

    # Output the agents' results and configurations
    for agent, config in zip(agent_list, agent_configs):
        print(f"Agent: {agent}, Config: {config}")

    # Additional logic for image agent interactions or other processes can be added here

if __name__ == "__main__":
    asyncio.run(main())