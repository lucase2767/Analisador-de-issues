import sys
import os
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

import pytest
from ai_agent import AIAgent

def test_analyze_issue_returns_valid_json(mocker):
    # Mock requests.post
    mock_post = mocker.patch('ai_agent.requests.post')
    mock_response = mocker.Mock()
    
    # Simular estrutura do JSON de retorno da API do Gemini
    mock_response.json.return_value = {
        'candidates': [{
            'content': {
                'parts': [{
                    'text': '```json\n{"categoria": "Bugfix", "prioridade": "alta", "resumo_curto": "Resumo de teste"}\n```'
                }]
            }
        }]
    }
    mock_post.return_value = mock_response

    # Instanciar o agente e chamar a função com titulo e body
    agent = AIAgent(api_key="fake_key")
    result = agent.analyze_issue("Test issue", "This is a bug that needs to be fixed.")

    # Validar resultados e assertivas
    expected = {"categoria": "Bugfix", "prioridade": "alta", "resumo_curto": "Resumo de teste"}
    assert result == expected
    mock_post.assert_called_once()
