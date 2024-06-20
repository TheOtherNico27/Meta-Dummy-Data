import json
import os
from config.github_client import GitHubClient
from helpers.url_parser import URLParser
from helpers.issue_extractor import IssueExtractor
from services.pull_request_service import PullRequestService
from services.issue_service import IssueService

def main(pr_url):

  gh_client = GitHubClient().get_client()

  owner,repo,pr_number = URLParser.parse_pr_url(pr_url)

  pr_service = PullRequestService(gh_client)
  pull_request = pr_service.get_pull_requests(owner, repo, pr_number)

  linked_issues = IssueExtractor.extract_linked_issues(pull_request.body)

  issue_service = IssueService(gh_client)
  issues_data = {}

  for issue in linked_issues:
    issue_owner = issue['owner'] if issue['owner'] else owner
    issue_repo = issue['repo'] if issue['repo'] else repo
    issue_details = issue_service.get_issue(issue_owner, issue_repo, issue['issue_number'])
    issues_data[f"{issue_owner}/{issue_repo}#{issue['issue_number']}"] =  issue_details.body

  print(json.dumps(issues_data, indent=2))




if __name__ == '__main__':
  pr_url = input("Enter the PR URL: ") #for testing purposes and will probably change later
  main(pr_url)



