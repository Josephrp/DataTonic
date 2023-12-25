import taskweaver
from taskweaver import TaskWeaverApp
from src.planner.planner import Planner
from taskweaver.code_generator.code_generator import CodeGenerator
from taskweaver.code_interpreter.code_interpreter import CodeInterpreter, CodeExecutor
from taskweaver.logging import TelemetryLogger
from taskweaver.memory import Memory

class TaskWeaverDataProcessor:
    def __init__(self, db_config, logger_config):
        self.taskweaver = TaskWeaver(db_config)
        self.planner = Planner()
        self.code_generator = CodeGenerator(self.taskweaver)
        self.code_executor = CodeExecutor(self.taskweaver)
        self.logger = TelemetryLogger(logger_config)
        self.memory = Memory() 
    def process_data_task(self, task_description):
        # Step 1: Create a plan based on the task description
        plan = self.planner.create_plan(task_description)
        
        # Step 2: Generate code for the plan
        code_post = self.code_generator.generate_code(plan, self.memory)
        
        # Step 3: Execute the generated code if it exists
        if code_post.attachments and code_post.attachments[-1].type == "code":
            code_snippet = code_post.attachments[-1].content
            execution_result = self.code_executor.execute_code(code_snippet)
            self.logger.log(execution_result)
            
            # Return the results of execution along with the code
            return {
                "code": code_snippet,
                "result": execution_result,
                "message": code_post.message 
            }
        else:
            self.logger.log(f"Failed to generate code: {code_post.message}")
            return {
                "message": code_post.message
            }
