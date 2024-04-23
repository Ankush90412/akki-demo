import os
import requests

def get_branch_contents(owner, repo, branch):
    headers = {"Authorization": f"token {os.getenv('GITHUB_TOKEN')}"}
    url = f"https://api.github.com/repos/{owner}/{repo}/contents/?ref={branch}"
    response = requests.get(url, headers=headers)
    response.raise_for_status()
    return response.json()

def check_same_code(owner, repo, pr_branch, dev_branch):
    pr_contents = get_branch_contents(owner, repo, pr_branch)
    dev_contents = get_branch_contents(owner, repo, dev_branch)
    
    pr_files = [file["name"] for file in pr_contents if file["type"] == "file"]
    dev_files = [file["name"] for file in dev_contents if file["type"] == "file"]
    
    return set(pr_files) == set(dev_files)

def block_pull_request(owner, repo, pr_number):
    headers = {"Authorization": f"token {os.getenv('GITHUB_TOKEN')}"}
    url = f"https://api.github.com/repos/{owner}/{repo}/pulls/{pr_number}/merge"
    data = {"merge_method": "squash", "commit_title": "PR blocked because dev branch doesn't have same code"}
    response = requests.put(url, headers=headers, json=data)
    response.raise_for_status()

if __name__ == "__main__":
    owner = "your_username"
    repo = "your_repository"
    pr_branch = "pull_request_branch"
    dev_branch = "dev"

    if not check_same_code(owner, repo, pr_branch, dev_branch):
        pr_number = os.getenv("INPUT_PULL_REQUEST_NUMBER")
        block_pull_request(owner, repo, pr_number)
        print("Pull request blocked because dev branch doesn't have the same code.")
    else:
        print("Pull request allowed because dev branch has the same code.")
