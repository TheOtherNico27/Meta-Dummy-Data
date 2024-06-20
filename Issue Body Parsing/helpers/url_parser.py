from urllib.parse import urlparse

class URLParser:
  @staticmethod
  def parse_pr_url(pr_url):
    path_segments = urlparse(pr_url).path.split('/').split('/')
    owner = path_segments[0]
    repo = path_segments[1]
    pr_number = path_segments[3]
    return owner, repo, pr_number
  
  
