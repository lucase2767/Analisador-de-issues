import os
from github import Github, GithubException
from dotenv import load_dotenv

load_dotenv()

class GitHubClient:
    def __init__(self, token: str): self.client = Github(token)

    def get_open_issues(self, repositorio: str):
        try:
            repo = self.client.get_repo(repositorio)
            return repo.get_issues(state='open')
        except GithubException as erro:
            print(f"Erro ao acessar repositório: {erro.data.get('message', erro)}")
            return []
