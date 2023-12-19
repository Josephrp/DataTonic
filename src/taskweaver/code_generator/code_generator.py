from taskweaver.code_executor import code_executor
from taskweaver.config import Config
from taskweaver.logging import Logger
from taskweaver.memory import Memory

class CodeGenerator:
    def __init__(self, interpreter: CodeInterpreter, config: Config, logger: Logger):
        self.interpreter = interpreter
        self.config = config
        self.logger = logger

    def verify_code(self, code_snippet: str) -> bool:
        """
        Verify the generated code snippet.
        Returns True if the code is verified, otherwise False.
        """
        allowed_modules = self.config.allowed_modules
        errors = self.interpreter.verify(code_snippet, allowed_modules)
        if errors:
            self.logger.error(f"Code verification error: {errors}")
            return False
        return True

    def generate_code(self, plan: dict, memory: Memory) -> str:
        """
        Generate code based on a plan. The code is then verified and executed.
        """
        code_snippet = self.interpreter.generate(plan, memory)
        
        if self.verify_code(code_snippet):
            # Execute the code if verification passes
            execution_result = self.interpreter.execute(code_snippet)
            return execution_result
        else:
            self.logger.error("Code verification failed.")
            return "Code verification failed."
