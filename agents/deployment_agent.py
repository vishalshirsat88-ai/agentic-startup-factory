from agents.agent_base import AgentBase
import subprocess
import os
import time
import re

class DeploymentAgent(AgentBase):
    def __init__(self):
        super().__init__("Deployment Agent")

    def deploy(self, build_message, idea_id=None): # New
        print("[Deployment Agent] Starting deployment pipeline...")
        try:
            path = build_message
            project_dir = os.path.basename(path)

            if not os.path.exists(path):
                return "Deployment failed: project folder not found"

            # 1. Initialize Railway Project
            print(f"[Deployment Agent] Initializing: {project_dir}")
            # We capture output to ensure it finishes before moving to link
            subprocess.run(["railway", "init", "--name", project_dir], cwd=path, capture_output=True)

            # 2. Link Local Folder (The "No-Argument" Fix)
            print(f"[Deployment Agent] Linking project context...")
            # Running 'railway link' without the project name argument 
            # tells it to use the project we just initialized in this directory.
            subprocess.run(["railway", "link"], cwd=path, check=False, capture_output=True)

            # 3. Deploy/Upload Code (The Non-Interactive Fix)
            print("[Deployment Agent] Running 'railway up'...")
            # Adding --detach stops the CLI from streaming logs, 
            # which often prevents the "select service" hang.
            subprocess.run(["railway", "up", "--detach"], cwd=path, check=False)

            # 4. Stability Wait (Increased slightly for domain generation)
            print("[Deployment Agent] Waiting 12s for URL generation...")
            time.sleep(12)

            # 5. Generate / Fetch Domain
            print("[Deployment Agent] Fetching public URL...")
            domain_process = subprocess.run(
                ["railway", "domain"],
                cwd=path,
                capture_output=True,
                text=True
            )

            domain_output = domain_process.stdout.strip()
            url_match = re.search(r'https://[^\s]+railway\.app', domain_output)
            
            if url_match:
                clean_url = url_match.group(0)
                print(f"\n🚀 STARTUP IS LIVE: {clean_url}\n")
                return f"Deployment successful: {clean_url}"

            # Fallback: Try to force-generate a domain if none exists
            print("[Deployment Agent] Domain not found, requesting generation...")
            subprocess.run(["railway", "domain"], cwd=path, check=False)
            
            return f"Deployment finished. Visit Railway Dashboard to view your URL."

        except Exception as e:
            print(f"[Deployment Agent] Error: {str(e)}")
            return f"Deployment failed: {str(e)}"