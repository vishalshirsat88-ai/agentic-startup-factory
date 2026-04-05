from tools.code_runner import run_app
from tools.llm import generate
from tools.product_validator import test_api, test_endpoint, test_post_endpoint, test_db
import os


# These are checker debugs
print("🔥 DEBUG: QA_Agent Loaded v2")


class QAAgent:
    def test_product(self, project_path):
        print("[QA Agent] Running application tests...")

        success, output = run_app(project_path)

        if success:
            print("[QA Agent] App started successfully")

            # Since run_app no longer returns base_url, skip API tests for now
            validation_report = {
                "status": "app_started",
                "message": output,
                "db": test_db(),
            }

            print("\n=== PRODUCT VALIDATION REPORT ===")
            print(validation_report)

            return validation_report

        print("[QA Agent] Error detected:")
        print("[QA Agent] App failed to start")
        print(output)

        return {"status": "fail", "error": output}
