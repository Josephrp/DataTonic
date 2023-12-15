from semantic_kernel.sdk import SemanticKernel
from taskweaver.taskweaver_module import TaskWeaverDataProcessor
from semantic_kernel.googleconnector import GoogleConnector
from sk_web_pages_plugin import WebPagesPlugin

class SemanticKernelDataModule:
    def __init__(self, google_api_key, google_search_engine_id):
        self.semantic_kernel = SemanticKernel()
        self.taskweaver_processor = TaskWeaverDataProcessor()
        self.google_connector = GoogleConnector(google_api_key, google_search_engine_id)
        self.web_pages_plugin = WebPagesPlugin()

        self.semantic_kernel.register_plugin('taskweaver', self.taskweaver_processor)
        self.semantic_kernel.register_plugin('web_pages', self.web_pages_plugin)


    async def process_data_with_taskweaver(self, task_description):
        taskweaver_processor = self.semantic_kernel.get_plugin('taskweaver')
        results = taskweaver_processor.process_data_task(task_description)
        return results

    async def perform_google_search(self, query, num_results=10, offset=0):
        search_results = await self.google_connector.search_async(query, num_results, offset)
        return search_results
    
    async def fetch_web_page_content(self, url):
        web_pages_plugin = self.semantic_kernel.get_plugin('web_pages')
        page_content = await web_pages_plugin.fetch_webpage(url)
        return page_content
    
    async def fetch_and_process_web_pages(self, query, num_results=10, offset=0):
        search_results = await self.perform_google_search(query, num_results, offset)
        page_contents = []
        for result in search_results:
            url = result['link']
            content = await self.fetch_web_page_content(url)
            processed_content = self.taskweaver_processor.process_data_task({'content': content})
            page_contents.append(processed_content)
        return page_contents
    