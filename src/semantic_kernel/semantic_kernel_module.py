from semantic_kernel import SemanticKernel
import taskweaver
from taskweaver.taskweaver_module import TaskWeaverDataProcessor
from semantic_kernel.googleconnector import GoogleConnector
from sk_web_pages_plugin import WebPagesPlugin
import asyncio
import sqlite3  # Assuming SQLite for simplicity

class TaskWeaverSQLIntegration:
    def __init__(self):
        self.taskweaver_processor = TaskWeaverDataProcessor(taskweaver.TaskWeaver())
        self.db_connection = sqlite3.connect('taskweaver_data.db')
        self.initialize_database()

    def initialize_database(self):
        self.db_connection.execute('''CREATE TABLE IF NOT EXISTS results (...);''')

    def process_and_store_data(self, task_data):
        results = self.taskweaver_processor.process_data_task(task_data)

        for result in results:
            self.db_connection.execute('INSERT INTO results VALUES (...)', (result,))
        self.db_connection.commit()

    def retrieve_data_for_planner(self, query):
        cursor = self.db_connection.execute(query)
        return cursor.fetchall()

    def close(self):
        self.db_connection.close()


async def create_sow_document():
    # Initialize SemanticKernelDataModule
    semantic_kernel_data_module = SemanticKernelDataModule('<google_api_key>', '<google_search_engine_id>')

    # Instantiate SoWPlanner with TaskWeaverDataProcessor
    sow_planner = SoWPlanner(semantic_kernel_data_module.taskweaver_processor)

    # Example project details (to be provided or retrieved)
    project_details = {
        "introduction": {
            "overview": "Brief description of the client's organization...",
            "purpose": "Clarification of the document's intent..."
        },
        # ... other sections
    }

    # Fetch the completed SoW plan
    completed_plan = await semantic_kernel_data_module.create_and_fetch_sow(project_details)
    return completed_plan

class SoWPlanner:
    def __init__(self, taskweaver_processor):
        self.taskweaver = taskweaver_processor

    async def generate_sow(self, project_details):
        sow_sections = {}
        for section, details in project_details.items():
            processed_section = await self.taskweaver.process_data_task({"section": section, "details": details})
            sow_sections[section] = processed_section
        return sow_sections

    # async def generate_sow(self, project_details):
    #     sow_sections = {
    #         "introduction": self.generate_introduction(project_details["introduction"]),
    #         "project_objectives_scope": self.generate_objectives_scope(project_details["objectives_scope"]),
    #         "project_approach_methodology": self.generate_approach_methodology(project_details["approach_methodology"]),
    #         "deliverables": self.generate_deliverables(project_details["deliverables"]),
    #         "timeline": self.generate_timeline(project_details["timeline"]),
    #         "roles_responsibilities": self.generate_roles_responsibilities(project_details["roles_responsibilities"]),
    #         "pricing_payment": self.generate_pricing_payment(project_details["pricing_payment"]),
    #         "confidentiality_legal_ethical": self.generate_confidentiality_legal_ethical(project_details["confidentiality_legal_ethical"]),
    #         "terms_conditions": self.generate_terms_conditions(project_details["terms_conditions"]),
    #         "signatures": self.generate_signatures(project_details["signatures"])
    #     }
    #     for section, details in project_details.items():
    #         processed_content = await self.taskweaver.process_data_task({'section': section, 'content': details})
    #         sow_sections[section] = processed_content
    #     return sow_sections

    def generate_introduction(self, intro_details):
        # TaskWeaver plugin for generating Introduction section
        return self.taskweaver.generate_section("introduction", intro_details)

    # Similarly, define methods for other sections
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
    
    async def create_and_fetch_sow(self, project_details):
        sow_planner = SoWPlanner(self.taskweaver_processor)
        sow_sections = await sow_planner.generate_sow(project_details)
        completed_plan = "\n".join([f"({key}) - {value}" for key, value in sow_sections.items()])
        return completed_plan
class SemanticKernelPlannerModule:
    def __init__(self):
        self.taskweaver_integration = TaskWeaverSQLIntegration()

    async def execute_planner_step(self, step_data):
        # Process data with TaskWeaver and store in SQL
        self.taskweaver_integration.process_and_store_data(step_data)

        # Retrieve specific data for the current step of the planner
        retrieved_data = self.taskweaver_integration.retrieve_data_for_planner("SELECT ... FROM results WHERE ...")
        return retrieved_data

    def close(self):
        self.taskweaver_integration.close()
        
if __name__ == "__main__":
    completed_sow_plan = asyncio.run(create_sow_document())
    print(completed_sow_plan)