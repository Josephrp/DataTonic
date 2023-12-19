# code_generator/code_generator.py

class CodeGenerator:
    def __init__(self, taskweaver):
        self.taskweaver = taskweaver

    def generate_code(self, plan):
        code_snippets = []
        for step in plan:
            # Assume taskweaver has a method to generate code for a given step
            generated_code = self.taskweaver.generate_code_for_step(step)
            code_snippets.append(generated_code)
        return code_snippets
