import os
import json
import logging
import requests

logging.basicConfig(level=logging.INFO, format="%(levelname)s: %(message)s")
logger = logging.getLogger(__name__)

class GitHubCommenter:
    def __init__(self):
        self.token = os.environ.get("GITHUB_TOKEN")
        self.repo = os.environ.get("GITHUB_REPOSITORY")
        self.event_path = os.environ.get("GITHUB_EVENT_PATH")
        self.workspace = os.environ.get("GITHUB_WORKSPACE", "")
        
        self.pr_number = None
        self.commit_sha = None
        self._load_event_data()

    def _load_event_data(self):
        if not self.event_path or not os.path.exists(self.event_path):
            logger.warning("GITHUB_EVENT_PATH not found. Cannot determine PR context.")
            return

        with open(self.event_path, "r") as f:
            event_data = json.load(f)
            
        if "pull_request" in event_data:
            self.pr_number = event_data["pull_request"]["number"]
            self.commit_sha = event_data["pull_request"]["head"]["sha"]
            logger.info(f"Detected PR #{self.pr_number} with commit {self.commit_sha}")
        else:
            logger.info("Not a pull request event. Inline commenting will be skipped.")

    def post_inline_comment(self, file_path: str, line_number: int, body: str):
        if not self.token or not self.repo or not self.pr_number or not self.commit_sha:
            logger.warning("Missing GitHub context (token, repo, pr_number, or commit_sha). Cannot post comment.")
            return

        # Ensure file_path is relative to the repo root
        if file_path.startswith(self.workspace):
            file_path = file_path[len(self.workspace):].lstrip("/")

        url = f"https://api.github.com/repos/{self.repo}/pulls/{self.pr_number}/comments"
        headers = {
            "Authorization": f"Bearer {self.token}",
            "Accept": "application/vnd.github.v3+json"
        }
        
        payload = {
            "body": f"🛡️ **Solidity Security Scanner PRO**\\n\\n{body}",
            "commit_id": self.commit_sha,
            "path": file_path,
            "line": line_number,
            "side": "RIGHT"
        }

        try:
            response = requests.post(url, headers=headers, json=payload)
            response.raise_for_status()
            logger.info(f"Successfully posted inline comment to {file_path}:{line_number}")
        except requests.exceptions.RequestException as e:
            logger.error(f"Failed to post inline comment: {e}")
            if hasattr(e, 'response') and e.response is not None:
                logger.error(f"Response: {e.response.text}")

    def post_general_comment(self, body: str):
        if not self.token or not self.repo or not self.pr_number:
            return
            
        url = f"https://api.github.com/repos/{self.repo}/issues/{self.pr_number}/comments"
        headers = {
            "Authorization": f"Bearer {self.token}",
            "Accept": "application/vnd.github.v3+json"
        }
        
        payload = {
            "body": f"🛡️ **Solidity Security Scanner PRO Report**\\n\\n{body}"
        }

        try:
            response = requests.post(url, headers=headers, json=payload)
            response.raise_for_status()
            logger.info(f"Successfully posted general PR comment.")
        except requests.exceptions.RequestException as e:
            logger.error(f"Failed to post general comment: {e}")
