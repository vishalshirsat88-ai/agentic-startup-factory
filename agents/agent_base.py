from tools.llm import generate

class AgentBase:

    def __init__(self, name):
        self.name = name

    def think(self, task):

        prompt = f"""
        You are {self.name} in an AI startup factory.

        Task:
        {task}

        Provide a concise professional response.
        """

        response = generate(prompt)

        print(f"[{self.name}] AI response:")
        print(response)

        return response


    def execute(self, task):

        prompt = f"""
        You are {self.name} responsible for executing tasks.

        Task:
        {task}

        Explain the execution steps clearly.
        """

        response = generate(prompt)

        print(f"[{self.name}] execution plan:")
        print(response)

        return response