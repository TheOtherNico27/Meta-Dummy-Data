import os
from github import Github

class GitHubClient:

  def __init__(self):
    token = os.getenv('GITHUB_TOKEN')
    self.gh = Github(login_or_token= token)#I will add my token in here in a bit with something like "export GITHUB_TOKEN = 'my_personal_access_token"
  
  def get_client(self):
    return self.gh
  

    

