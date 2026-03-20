from tools.code_runner import run_app
from tools.llm import generate
import os

class QAAgent:

    def test_product(self, project_path):

        print("[QA Agent] Running application tests...")

        success, output = run_app(project_path)

        if success:
            print("[QA Agent] App started successfully")
            return True

        print("[QA Agent] Error detected:")
        print(output)

        return output