class IssueService:
  def __init__(self, gh_client):
   self.gh_client = gh_client

  def get_issue(self, owner, repo, issue_number):
    repo = self.gh_client.get_repo(f"{owner}/{repo}")
    return repo.get_issue(number= issue_number)