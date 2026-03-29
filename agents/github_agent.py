from github import Github
import os
import subprocess


class GitHubAgent:
    def __init__(self):
        token = os.getenv("GH_PAT")

        print("DEBUG GH_PAT:", "SET" if token else "NOT SET")

        if not token:
            raise Exception("GH_PAT is missing")

        self.github = Github(token)
        self.user = self.github.get_user()

    def create_repo_and_push(self, project_name):
        print("[GitHub Agent] pushing to main factory repo...")

        project_path = f"projects/{project_name}"

        # ✅ DEFINE ROOT PATH FIRST (CRITICAL FIX)
        root_path = os.path.abspath(os.path.join(os.path.dirname(__file__), ".."))

        # 🔐 Ensure authenticated remote (AFTER root_path is defined)
        token = os.getenv("GH_PAT")
        repo_name = "agentic-startup-factory"

        remote_url = f"https://{token}@github.com/{self.user.login}/{repo_name}.git"

        subprocess.run(
            ["git", "remote", "set-url", "origin", remote_url],
            cwd=root_path,
            stderr=subprocess.DEVNULL,
        )

        # 🔍 Check git repo exists
        if not os.path.exists(os.path.join(root_path, ".git")):
            print("[GitHub Agent] ERROR: Not a git repository")
            return "Git not initialized"

        # 🔍 Check project exists
        full_project_path = os.path.join(root_path, project_path)
        if not os.path.exists(full_project_path):
            print(f"[GitHub Agent] ERROR: Project not found: {project_path}")
            return "Project path missing"

        # ✅ ADD
        add = subprocess.run(
            ["git", "add", project_path, "CODEBASE_CONTEXT.md"],
            cwd=root_path,
            capture_output=True,
            text=True,
        )

        if add.returncode != 0:
            print("[GitHub Agent] git add failed:")
            print(add.stderr)
            return "Git add failed"

        # ✅ COMMIT
        commit = subprocess.run(
            ["git", "commit", "-m", f"Add project: {project_name}"],
            cwd=root_path,
            capture_output=True,
            text=True,
        )

        if "nothing to commit" in (commit.stdout + commit.stderr).lower():
            print("[GitHub Agent] Nothing to commit")
        elif commit.returncode != 0:
            print("[GitHub Agent] Commit failed:")
            print(commit.stderr)
            return "Commit failed"
        else:
            print("[GitHub Agent] Commit successful")

        # ✅ PUSH
        push = subprocess.run(
            ["git", "push"], cwd=root_path, capture_output=True, text=True
        )

        if push.returncode != 0:
            print("[GitHub Agent] Push failed:")
            print(push.stderr)

            if "authentication" in push.stderr.lower():
                print("[GitHub Agent] Likely GH_PAT issue")

            return "Push failed"

        print("[GitHub Agent] Push successful")

        return "Updated main factory repo"
