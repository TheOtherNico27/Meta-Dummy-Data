import re

class IssueExtractor:
    @staticmethod
    def extract_linked_issues(body):
        regex = re.compile(r'(close|closes|closed|fix|fixes|fixed|resolve|resolves|resolved)\s+(#\d+|[\w-]+\/[\w-]+#\d+)', re.IGNORECASE)
        matches = regex.findall(body)
        issues = []

        for match in matches:
            keyword, issue = match
            if '/' in issue:
                owner_repo, issue_number = issue.split('#')
                owner, repo = owner_repo.split('/')
            else:
                owner = None
                repo = None
                issue_number = int(issue.lstrip('#'))
            issues.append({
                'keyword': keyword,
                'owner': owner,
                'repo': repo,
                'issue_number': issue_number
            })
        return issues