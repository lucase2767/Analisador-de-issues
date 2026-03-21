import os
import json
import requests
from dotenv import load_dotenv

load_dotenv()

class AIAgent:
    def __init__(self, api_key: str):
        self.api_key = api_key
        self.url = f"https://generativelanguage.googleapis.com/v1beta/models/gemini-flash-latest:generateContent?key={self.api_key}"

    def analyze_issue(self, titulo: str, body: str):
        prompt = f"""
        Analise a seguinte issue do GitHub e retorne APENAS um JSON no formato:
        {{
            "categoria": "Bugfix" | "Melhoria" | "Pergunta" | "Documentação" | "Outro",
            "prioridade": "baixa" | "média" | "alta",
            "resumo_curto": "string de no máximo 100 caracteres"
        }}

        Issue:
        Título: {titulo}
        Descrição: {body}
        """

        payload = {
            "contents": [{
                "parts": [{"text": prompt}]
            }]
        }

        try:
            response = requests.post(self.url, json=payload, timeout=10)
            response.raise_for_status()
            
            result = response.json()
            raw_text = result['candidates'][0]['content']['parts'][0]['text'].strip()
            
            # Para limpar o texto e extrair apenas o JSON, caso esteja formatado como código
            if raw_text.startswith("```json"):
                raw_text = raw_text[7:-3].strip()
            elif raw_text.startswith("```"):
                raw_text = raw_text[3:-3].strip()
            
            return json.loads(raw_text)
        except Exception as e:
            print(f"Erro na análise da IA: {e}")
            return {
                "categoria": "erro",
                "prioridade": "indefinida",
                "resumo_curto": "Não foi possível analisar esta issue por erro na API."
            }
