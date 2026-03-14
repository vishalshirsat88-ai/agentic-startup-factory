from github import Github
import os
import subprocess


class GitHubAgent:

    def __init__(self):
        token = os.getenv("GH_PAT")
        self.github = Github(token)
        self.user = self.github.get_user()

    def create_repo_and_push(self, project_name):

        print("[GitHub Agent] preparing repository...")

        try:
            repo = self.user.get_repo(project_name)
            print("[GitHub Agent] repo already exists")
        except:
            repo = self.user.create_repo(project_name, private=False)
            print("[GitHub Agent] repository created")

        project_path = f"projects/{project_name}"
        os.makedirs(project_path, exist_ok=True)

        subprocess.run(["git", "init"], cwd=project_path)
        subprocess.run(["git", "add", "."], cwd=project_path)
        subprocess.run(["git", "commit", "-m", "initial commit"], cwd=project_path)

        repo_url = repo.clone_url

        subprocess.run(["git", "remote", "remove", "origin"], cwd=project_path, stderr=subprocess.DEVNULL)
        token = os.getenv("GH_PAT")

        remote_url = f"https://{token}@github.com/{self.user.login}/{project_name}.git"

        subprocess.run(["git", "remote", "add", "origin", remote_url], cwd=project_path)

        subprocess.run(["git", "branch", "-M", "main"], cwd=project_path)
        subprocess.run(["git", "push", "-u", "origin", "main"], cwd=project_path)

        return repo.html_url