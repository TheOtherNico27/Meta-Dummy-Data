class PullRequestService:
  def __init__(self, gh_client):
    self.gh_client = gh_client

    def get_pull_requests(self, owner, repo, pr_number):
      repo = self.gh_client.get_repo(f"{owner}/{repo}")
      return repo.get_pull(pr_number)
    
    