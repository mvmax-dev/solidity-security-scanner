#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Maxwell VOSS — Viral Growth Hacker Bot
Automated Marketing & Distribution via GitHub Pull Requests.

This bot hunts for high-profile Web3 repositories (Solidity/Rust), forks them,
injects our Security Scanner GitHub Action, and opens a Pull Request.
This initiates the viral loop described in the Investment Memo.
"""

import os
import sys
import time
import json
import base64
import requests
import argparse
from datetime import datetime

# Configure logging
def _log(tag, msg):
    print(f"[{tag}] {msg}")

GITHUB_TOKEN = os.environ.get("GITHUB_TOKEN")
if not GITHUB_TOKEN:
    # Try to get it from gh cli
    try:
        import subprocess
        GITHUB_TOKEN = subprocess.check_output(["gh", "auth", "token"]).decode().strip()
    except Exception:
        pass

if not GITHUB_TOKEN:
    _log("FATAL", "GITHUB_TOKEN environment variable is missing.")
    sys.exit(1)

HEADERS = {
    "Authorization": f"Bearer {GITHUB_TOKEN}",
    "Accept": "application/vnd.github.v3+json",
    "X-GitHub-Api-Version": "2022-11-28"
}

API_URL = "https://api.github.com"
MARKETPLACE_URL = "https://github.com/marketplace/actions/automated-smart-contract-auditor-pro"

# The workflow template to inject
WORKFLOW_PATH = ".github/workflows/security-audit-pro.yml"
WORKFLOW_CONTENT = """name: "Web3 Security Audit"
on: [pull_request]

jobs:
  audit:
    runs-on: ubuntu-latest
    steps:
      - uses: actions/checkout@v4

      - name: Run Automated Smart Contract Auditor PRO
        uses: mvmax-dev/solidity-security-scanner@main
        with:
          github_token: ${{ secrets.GITHUB_TOKEN }}
"""

PR_TITLE = "🛡️ Chore: Integrate Automated Smart Contract Auditor PRO"
PR_BODY = f"""### 🚀 Enhance Security Posture with Automated Smart Contract Auditor PRO

Hello Maintainers! 👋

I noticed your project uses Solidity/Rust, so I've integrated the **[Automated Smart Contract Auditor PRO]({MARKETPLACE_URL})** into your GitHub Actions workflow.

This tool runs automatically on every Pull Request to provide:
- **Instant AST Structural Analysis** for Reentrancy, Access Control, and Flash Loan vulnerabilities.
- **Gas Optimization Suggestions** line-by-line.
- **False-Positive Suppression** (No more noisy Slither alerts).

It's 100% free for open-source projects. 

*If you prefer not to use it, feel free to close this PR. We're just a team of security researchers trying to make Web3 a safer place.* 🛡️

---
**Learn more:** [GitHub Marketplace - Security Scanner PRO]({MARKETPLACE_URL})
"""

class ViralGrowthBot:
    def __init__(self, username="mvmax-dev"):
        self.username = username
        self.tracked_repos_file = os.path.join(os.path.dirname(os.path.abspath(__file__)), "targeted_repos.json")
        self.targeted = self._load_targeted()

    def _load_targeted(self):
        if os.path.exists(self.tracked_repos_file):
            try:
                with open(self.tracked_repos_file, "r") as f:
                    return json.load(f)
            except:
                pass
        return []

    def _save_targeted(self, repo_full_name):
        self.targeted.append(repo_full_name)
        with open(self.tracked_repos_file, "w") as f:
            json.dump(self.targeted, f)

    def search_repositories(self, language="solidity", min_stars=50, limit=5):
        """Finds repos that we haven't targeted yet."""
        _log("RECON", f"Hunting for {language} repositories with >{min_stars} stars...")
        query = f"language:{language} stars:>{min_stars} fork:false"
        url = f"{API_URL}/search/repositories?q={query}&sort=updated&order=desc&per_page=50"
        
        response = requests.get(url, headers=HEADERS)
        response.raise_for_status()
        
        items = response.json().get("items", [])
        candidates = []
        
        for item in items:
            full_name = item["full_name"]
            if full_name not in self.targeted and item["owner"]["login"].lower() != self.username.lower():
                candidates.append(item)
                if len(candidates) >= limit:
                    break
                    
        _log("RECON", f"Found {len(candidates)} prime targets.")
        return candidates

    def fork_repository(self, repo_full_name):
        """Forks the repo and waits for it to be ready."""
        _log("HACK", f"Forking {repo_full_name}...")
        url = f"{API_URL}/repos/{repo_full_name}/forks"
        response = requests.post(url, headers=HEADERS)
        
        if response.status_code == 202:
            forked_repo = response.json()["full_name"]
            _log("HACK", f"Fork initiated: {forked_repo}. Waiting 10 seconds for completion...")
            time.sleep(10) # Wait for fork to complete on GitHub's backend
            return forked_repo
        elif response.status_code == 403:
             _log("ERROR", f"Fork failed: {response.text}")
             return None
        else:
             # Already forked?
             response = requests.get(f"{API_URL}/repos/{self.username}/{repo_full_name.split('/')[1]}", headers=HEADERS)
             if response.status_code == 200:
                 _log("HACK", f"Already forked: {response.json()['full_name']}")
                 return response.json()['full_name']
             response.raise_for_status()

    def get_default_branch(self, repo_full_name):
        url = f"{API_URL}/repos/{repo_full_name}"
        res = requests.get(url, headers=HEADERS)
        res.raise_for_status()
        return res.json().get("default_branch", "main")

    def get_branch_sha(self, repo_full_name, branch):
        url = f"{API_URL}/repos/{repo_full_name}/git/refs/heads/{branch}"
        res = requests.get(url, headers=HEADERS)
        if res.status_code == 200:
            return res.json()["object"]["sha"]
        return None

    def create_branch(self, repo_full_name, new_branch, sha):
        _log("HACK", f"Creating branch '{new_branch}' on {repo_full_name}...")
        url = f"{API_URL}/repos/{repo_full_name}/git/refs"
        data = {
            "ref": f"refs/heads/{new_branch}",
            "sha": sha
        }
        res = requests.post(url, headers=HEADERS, json=data)
        if res.status_code in [201, 422]: # 422 usually means it already exists
            return True
        res.raise_for_status()

    def inject_workflow(self, repo_full_name, branch):
        _log("INJECT", f"Injecting Security Scanner Action into {WORKFLOW_PATH}...")
        url = f"{API_URL}/repos/{repo_full_name}/contents/{WORKFLOW_PATH}"
        
        # Check if file exists to get SHA (for update vs create)
        res_get = requests.get(url + f"?ref={branch}", headers=HEADERS)
        file_sha = None
        if res_get.status_code == 200:
            file_sha = res_get.json()["sha"]
            
        data = {
            "message": "Add Automated Smart Contract Auditor PRO workflow",
            "content": base64.b64encode(WORKFLOW_CONTENT.encode("utf-8")).decode("utf-8"),
            "branch": branch
        }
        if file_sha:
            data["sha"] = file_sha
            
        res = requests.put(url, headers=HEADERS, json=data)
        res.raise_for_status()
        _log("INJECT", "Injection successful.")

    def create_pull_request(self, upstream_repo, fork_owner, branch, default_branch):
        _log("VIRAL", f"Opening Pull Request to {upstream_repo}...")
        url = f"{API_URL}/repos/{upstream_repo}/pulls"
        data = {
            "title": PR_TITLE,
            "head": f"{fork_owner}:{branch}",
            "base": default_branch,
            "body": PR_BODY
        }
        res = requests.post(url, headers=HEADERS, json=data)
        if res.status_code == 201:
            pr_url = res.json()["html_url"]
            _log("VIRAL", f"✅ SUCCESS! Pull Request Opened: {pr_url}")
            return True
        else:
            _log("ERROR", f"Failed to open PR: {res.text}")
            return False

    def hack_the_planet(self, language="solidity", max_targets=1, dry_run=False):
        _log("INIT", f"Initializing Viral Growth Bot [Target: {language}] [Max: {max_targets}]")
        targets = self.search_repositories(language=language, limit=max_targets)
        
        if not targets:
            _log("EXIT", "No new targets found.")
            return

        for target in targets:
            upstream_repo = target["full_name"]
            _log("TARGET", f"Engaging target: {upstream_repo}")
            
            if dry_run:
                _log("DRY RUN", f"Would fork {upstream_repo}, inject workflow, and open PR.")
                self._save_targeted(upstream_repo)
                continue

            try:
                # 1. Fork
                forked_repo = self.fork_repository(upstream_repo)
                if not forked_repo:
                    continue
                fork_owner = forked_repo.split('/')[0]

                # 2. Setup Branches
                default_branch = self.get_default_branch(upstream_repo)
                sha = self.get_branch_sha(forked_repo, default_branch)
                if not sha:
                    _log("ERROR", "Could not find default branch SHA.")
                    continue
                    
                new_branch = "add-security-scanner"
                self.create_branch(forked_repo, new_branch, sha)
                
                # Wait for branch to be available
                time.sleep(2)

                # 3. Inject Payload
                self.inject_workflow(forked_repo, new_branch)
                
                # Wait for commit to propagate
                time.sleep(3)

                # 4. Open PR
                success = self.create_pull_request(upstream_repo, fork_owner, new_branch, default_branch)
                
                if success:
                    self._save_targeted(upstream_repo)
                    
            except Exception as e:
                _log("FATAL", f"Error engaging {upstream_repo}: {e}")

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Viral Growth Bot")
    parser.add_argument("--language", default="solidity", help="Language to target")
    parser.add_argument("--max", type=int, default=1, help="Max targets to engage")
    parser.add_argument("--dry-run", action="store_true", help="Don't actually open PRs")
    args = parser.parse_args()

    bot = ViralGrowthBot()
    bot.hack_the_planet(language=args.language, max_targets=args.max, dry_run=args.dry_run)
