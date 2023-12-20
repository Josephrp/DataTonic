import json
import asyncio
import os
from src.semantic_kernel.semantic_kernel_module import SemanticKernelDataModule
from src.taskweaver.taskweaver_module import TaskWeaverDataProcessor
from src.autogen.autogen_module import AutoGenModule

async def main():
    # Load the configuration list for different LLMs
    with open('OAI_CONFIG_LIST.json', 'r') as file:
        OAI_CONFIG_LIST = json.load(file)

    # Initialize the AutoGenModule with the Semantic Kernel and Taskweaver modules
    semantic_kernel = SemanticKernelDataModule()
    taskweaver = TaskWeaverDataProcessor()
    autogen_module = AutoGenModule(memgpt_memory_path="<path_to_memgpt_memory>", openai_api_key=os.getenv('OPENAI_API_KEY'))

    # Inject dependencies into AutoGenModule
    autogen_module.semantic_kernel = semantic_kernel
    autogen_module.taskweaver = taskweaver

    # Get user input to initiate the process
    user_input = input("Please provide a description for the task you'd like to perform: ")

    # Process the user input using AutoGenModule
    executed_plan = await autogen_module.process_user_input(user_input)

    # Output the result of the executed plan
    print(f"Executed Plan: \n{executed_plan}")

if __name__ == "__main__":
    asyncio.run(main())