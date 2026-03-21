import os
import sys
from dotenv import load_dotenv
from github_client import GitHubClient
from ai_agent import AIAgent

load_dotenv()

def main():
    github_token = os.getenv("GITHUB_TOKEN")
    gemini_key = os.getenv("GEMINI_API_KEY")
    repositorio = os.getenv("REPOSITORY_NAME")

    if not all([github_token, gemini_key, repositorio]):
        print("Erro: Verifique se as chaves GITHUB_TOKEN, GEMINI_API_KEY e REPOSITORY_NAME estão no .env")
        sys.exit(1)

    gh_client = GitHubClient(github_token)
    ai_agent = AIAgent(gemini_key)

    print(f"Buscando issues em: {repositorio}...\n")
    issues = gh_client.get_open_issues(repositorio)

    for issue in issues:
        print(f"--- Issue #{issue.number}: {issue.title} ---")
        
        if not issue.pull_request:
            triage = ai_agent.analyze_issue(issue.title, issue.body or "")
            
            print(f"Categoria: {triage.get('categoria')}")
            print(f"Prioridade: {triage.get('prioridade')}")
            print(f"Resumo: {triage.get('resumo_curto')}")
            print("-" * 50)

if __name__ == "__main__":
    main()
