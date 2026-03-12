class AgentBase:
    def __init__(self, name):
        self.name = name

    def think(self, task):
        print(f"[{self.name}] thinking about: {task}")
        return f"{self.name} suggests action for: {task}"

    def execute(self, task):
        print(f"[{self.name}] executing task: {task}")
        return f"{self.name} completed: {task}"