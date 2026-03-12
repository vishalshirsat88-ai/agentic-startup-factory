import os

files = {

"agents/agent_base.py": '''
class AgentBase:
    def __init__(self, name):
        self.name = name

    def think(self, task):
        print(f"[{self.name}] thinking about: {task}")
        return f"{self.name} suggests action for: {task}"

    def execute(self, task):
        print(f"[{self.name}] executing task: {task}")
        return f"{self.name} completed: {task}"
''',

"agents/ceo_agent.py": '''
from agents.agent_base import AgentBase

class CEOAgent(AgentBase):
    def __init__(self):
        super().__init__("CEO Agent")

    def generate_idea(self):
        return self.think("Generate startup idea")
''',

"agents/cto_agent.py": '''
from agents.agent_base import AgentBase

class CTOAgent(AgentBase):
    def __init__(self):
        super().__init__("CTO Agent")

    def design_architecture(self, idea):
        return self.think(f"Design architecture for {idea}")
''',

"agents/developer_agent.py": '''
from agents.agent_base import AgentBase

class DeveloperAgent(AgentBase):
    def __init__(self):
        super().__init__("Developer Agent")

    def build_feature(self, architecture):
        return self.execute(f"Build MVP for {architecture}")
''',

"agents/qa_agent.py": '''
from agents.agent_base import AgentBase

class QAAgent(AgentBase):
    def __init__(self):
        super().__init__("QA Agent")

    def test_product(self, build):
        return self.execute(f"Testing {build}")
''',

"agents/growth_agent.py": '''
from agents.agent_base import AgentBase

class GrowthAgent(AgentBase):
    def __init__(self):
        super().__init__("Growth Agent")

    def launch_marketing(self, product):
        return self.execute(f"Launch marketing for {product}")
''',

"agents/finance_agent.py": '''
from agents.agent_base import AgentBase

class FinanceAgent(AgentBase):
    def __init__(self):
        super().__init__("Finance Agent")

    def track_revenue(self, product):
        return self.execute(f"Tracking revenue for {product}")
''',

"agents/deployment_agent.py": '''
from agents.agent_base import AgentBase

class DeploymentAgent(AgentBase):
    def __init__(self):
        super().__init__("Deployment Agent")

    def deploy(self, build):
        return self.execute(f"Deploying {build}")
''',

"orchestrator/orchestrator.py": '''
from agents.ceo_agent import CEOAgent
from agents.cto_agent import CTOAgent
from agents.developer_agent import DeveloperAgent
from agents.qa_agent import QAAgent
from agents.deployment_agent import DeploymentAgent
from agents.growth_agent import GrowthAgent
from agents.finance_agent import FinanceAgent

MODE = "controlled"

class Orchestrator:

    def __init__(self):
        self.ceo = CEOAgent()
        self.cto = CTOAgent()
        self.dev = DeveloperAgent()
        self.qa = QAAgent()
        self.deploy = DeploymentAgent()
        self.growth = GrowthAgent()
        self.finance = FinanceAgent()

    def run_startup_cycle(self):

        idea = self.ceo.generate_idea()
        print(idea)

        approval = input("Approve idea? (y/n): ")
        if approval != "y":
            print("Idea rejected")
            return

        arch = self.cto.design_architecture(idea)
        print(arch)

        build = self.dev.build_feature(arch)
        print(build)

        test = self.qa.test_product(build)
        print(test)

        deploy = self.deploy.deploy(build)
        print(deploy)

        marketing = self.growth.launch_marketing(build)
        print(marketing)

        revenue = self.finance.track_revenue(build)
        print(revenue)

if __name__ == "__main__":
    o = Orchestrator()
    o.run_startup_cycle()
''',

"dashboard/dashboard.py": '''
from flask import Flask, jsonify
from orchestrator.orchestrator import Orchestrator

app = Flask(__name__)
orch = Orchestrator()

@app.route("/")
def home():
    return "Founder Control Room Dashboard Running"

@app.route("/run_cycle")
def run_cycle():
    orch.run_startup_cycle()
    return jsonify({"status": "cycle started"})

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
''',

"tools/web_search.py": '''
def web_search(query):
    return f"Searching web for {query}"
''',

"tools/github_tool.py": '''
def push_code(repo):
    return f"Pushing code to {repo}"
''',

"tools/deployment_tool.py": '''
def deploy_app(name):
    return f"Deploying {name}"
''',

"tools/research_tool.py": '''
def market_research(topic):
    return f"Researching {topic}"
'''
}

for path, content in files.items():
    os.makedirs(os.path.dirname(path), exist_ok=True)
    with open(path, "w") as f:
        f.write(content.strip())

print("✅ All files populated successfully.")