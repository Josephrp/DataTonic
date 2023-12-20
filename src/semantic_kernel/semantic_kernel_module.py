from semantic_kernel import SemanticKernel, KernelBuilder
from taskweaver.taskweaver_module import TaskWeaverDataProcessor
from semantic_kernel.plugins.taskweaverplugin import TaskWeaverSQLIntegration
from semantic_kernel.plugins.googleconnector import GoogleConnector
from semantic_kernel.plugins.sk_web_pages_plugin import WebPagesPlugin
import asyncio

project_details = {
        "Overview": {
            "Background": "In-depth background information about the target organization and history.",
            "ProjectRationale": "Explanation of why the project is being undertaken and its importance."
        },
        "ProjectGoalsAndScope": {
            "PrimaryObjectives": "Key objectives the project aims to achieve.",
            "SecondaryObjectives": "Additional objectives that add value to the project.",
            "ScopeInclusions": "Explicitly what is included in the project's scope.",
            "ScopeExclusions": "Explicitly what is excluded from the project's scope.",
            "KeyPerformanceIndicators": "Metrics to measure the project's success."
        },

        "MethodologyAndWorkflow": {
            "ProjectMethodology": "Detailed description of the methodologies to be applied.",
            "WorkflowStrategy": "Strategy for workflow management across the project.",
            "MilestonePlanning": "Breakdown of key project milestones.",
            "TaskAllocation": "Allocation of tasks within each project phase.",
            "QualityAssuranceProcesses": "Processes in place to ensure the quality of work."
        },

        "ExpectedDeliverables": {
            "CoreDeliverables": "List of primary deliverables to be produced.",
            "SupportingDeliverables": "Supplementary deliverables that support core outputs.",
            "DeliveryStandards": "Standards and specifications for deliverable quality.",
            "PresentationRequirements": "Requirements for the presentation of deliverables.",
            "FeedbackAndRevisions": "Process for providing feedback and making revisions."
        },

        # "ProjectTimelineAndMilestones": {
        #     "DetailedTimeline": "Comprehensive timeline with start and end dates, phase durations, and key milestones.",
        #     "ProgressReviewCheckpoints": "Pre-defined intervals for reviewing project progress and making adjustments."
        # },
        "ResourceAllocationAndRoles": {
            "TeamStructure": "Description of the project team's composition and hierarchy.",
            "RoleResponsibilities": "Specific responsibilities assigned to each team role.",
        #   "ResourcePlanning": "Detailed plan for allocating resources throughout the project.",
        #   "SkillDevelopment": "Opportunities for team skill development and training.",
        #   "StakeholderEngagement": "Plan for engaging stakeholders throughout the project."
        },
        "BudgetAndCosting": {
            "BudgetBreakdown": "Detailed budget allocation for different project components.",
            "CostControlMeasures": "Measures in place to control costs and handle budget overruns."
        },
        "RiskManagementPlan": {
            "IdentifiedRisks": "List of potential risks and their impact on the project.",
            "MitigationStrategies": "Strategies for managing and mitigating these risks."
        },
        "LegalAndCompliance": {
            "RegulatoryRequirements": "Overview of legal and regulatory requirements relevant to the project.",
            "ComplianceStrategy": "Approach to ensuring compliance with these requirements."
        }
    }

async def create_sow_document():
    semantic_kernel_data_module = SemanticKernelDataModule('<google_api_key>', '<google_search_engine_id>')
    sow_planner = SoWPlanner(semantic_kernel_data_module.process_data_with_taskweaver)
    completed_plan = await sow_planner.generate_sow(project_details)
    return completed_plan

class SoWPlanner:
    def __init__(self, process_data_function):
        self.process_data = process_data_function

    async def generate_sow(self, project_details):
        sow_document = ""
        for section, details in project_details.items():
            processed_section = await self.process_data({'section': section, 'details': details})
            sow_document += f"{section}:\n"
            for sub_section, content in processed_section.items():
                sow_document += f"  {sub_section}: {content}\n"
            sow_document += "\n"  

        return sow_document
class SemanticKernelDataModule:
    def __init__(self, google_api_key, google_search_engine_id):
        self.kernel = SemanticKernel()
        self.kernel_builder = KernelBuilder()
        self.taskweaver_integration = TaskWeaverSQLIntegration()
        self.google_connector = GoogleConnector(google_api_key, google_search_engine_id)
        self.web_pages_plugin = WebPagesPlugin()
        self.kernel.Plugins.RegisterPlugin('taskweaver', self.taskweaver_integration)
        self.kernel.Plugins.RegisterPlugin('google', self.google_connector)
        self.kernel.Plugins.RegisterPlugin('web_pages', self.web_pages_plugin)
        self.kernel.Plugins.RegisterPlugin('taskweaver', self.taskweaver_processor)
        self.kernel.Plugins.RegisterPlugin('google', self.google_connector)
        self.kernel.Plugins.RegisterPlugin('webpages', self.web_pages_plugin)

        # Adding prompt directories
        # self.kernel_builder.Plugins.AddPromptDirectory('sow_prompts', '/path/to/sow/prompts')

    async def create_and_fetch_sow(self, project_details):
        # Process data using TaskWeaver and store it using SQL integration
        sow_planner = SoWPlanner(self.taskweaver_processor)
        sow_sections = await sow_planner.generate_sow(project_details)
        completed_plan = "\n".join([f"({key}) - {value}" for key, value in sow_sections.items()])
        return completed_plan

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
        sow_planner = SoWPlanner(self.taskweaver_integration)
        for section, details in project_details.items():
            self.taskweaver_integration.process_and_store_data({'section': section, 'details': details})
        sow_document = await sow_planner.generate_sow(project_details.keys())
        return sow_document

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

async def create_sow_document():
    # Initialize SemanticKernelDataModule
    semantic_kernel_data_module = SemanticKernelDataModule('<google_api_key>', '<google_search_engine_id>')

    # Fetch the completed SoW plan using SemanticKernelDataModule
    completed_plan = await semantic_kernel_data_module.create_and_fetch_sow(project_details)
    return completed_plan

# Assuming the rest of the SemanticKernelDataModule and related classes are defined as previously described

if __name__ == "__main__":
    completed_sow_plan = asyncio.run(create_sow_document())
    print(completed_sow_plan)