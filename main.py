import json
import os
import asyncio
from chainlit import chainlit as cl
from src.semantic_kernel.semantic_kernel_module import SemanticKernelDataModule
from src.tonicweaver.taskweaver_module import TaskWeaverDataProcessor
from src.autogen.autogen_module import AutoGenModule

async def process_user_input(user_input):
    semantic_kernel = SemanticKernelDataModule()
    taskweaver = TaskWeaverDataProcessor()
    autogen_module = AutoGenModule(memgpt_memory_path="./src/autogen/MemGPT", openai_api_key=os.getenv('OPENAI_API_KEY'))
    
    autogen_module.semantic_kernel = semantic_kernel
    autogen_module.taskweaver = taskweaver
    
    sow_document = await semantic_kernel.create_and_fetch_sow(user_input)
    
    executed_plan = await autogen_module.AutoGenModule(sow_document)
    
    return executed_plan

@cl.on_chat_start
async def start():
    # Initial setup if needed
    pass

@cl.on_message
async def main(message: cl.Message):
    user_input = message.content
    executed_plan = await process_user_input(user_input)
    
    # Assuming the executed_plan is a string or something that can be converted to a string
    await cl.Message(content=str(executed_plan)).send()

if __name__ == "__main__":
    cl.run(main)