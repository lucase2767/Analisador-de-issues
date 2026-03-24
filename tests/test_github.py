import sys
import os
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

import pytest
from github_client import GitHubClient

def test_get_open_issues_returns_list(mocker):
    # Mock da biblioteca Github
    mock_github_class = mocker.patch('github_client.Github')
    mock_client = mock_github_class.return_value
    mock_repo = mocker.Mock()
    
    # Configurar mocks encadeados
    mock_client.get_repo.return_value = mock_repo
    
    # Criar issues mockadas
    mock_issue1 = mocker.Mock()
    mock_issue1.title = "Issue numero 1"
    mock_issue2 = mocker.Mock()
    mock_issue2.title = "Issue numero 2"
    
    mock_repo.get_issues.return_value = [mock_issue1, mock_issue2]

    # Instanciar e testar
    client = GitHubClient(token="fake_token")
    issues = client.get_open_issues("fake_owner/fake_repo")

    # Validar asserts usando a lista retornada
    assert len(issues) == 2
    assert issues[0].title == "Issue numero 1"
    assert issues[1].title == "Issue numero 2"
    
    # Verificar garantias e chamadas do client
    mock_client.get_repo.assert_called_once_with("fake_owner/fake_repo")
    mock_repo.get_issues.assert_called_once_with(state='open')
