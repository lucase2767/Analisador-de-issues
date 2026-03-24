# Resumo de issues do GitHub automatico

Este é o primeiro projeto que utiliza uma LLM ja pronta para automação de issues no GitHub, classificando-as por categoria, prioridade e gerando um resumo curto.

## 🚀 Como Executar

1.  Crie e ative um ambiente virtual:
    ```bash
    python -m venv .venv
    .venv\Scripts\activate
    ```

2.  Instale as dependências:
    ```bash
    pip install -r requirements.txt
    ```

3.  Configure as variáveis de ambiente:
    Copie e cole o arquivo `.env.example` e renome-o para `.env` ou:
    ```bash
    cp .env.example .env
    ```
    e preencha com suas chaves


4.  Execute o script:
    ```bash
    python main.py
    ```

## 🧪 Como Rodar os Testes

Para executar os testes unitários da aplicação, basta rodar o comando abaixo na raiz do projeto:

```bash
pytest
```

## Estratégia de Prompting

Para garantir que a IA retorne sempre um JSON válido, o prompt no `ai_agent.py` foi estruturado da seguinte forma:

1.  **Restrição de Formato**: O prompt começa com a instrução explícita "retorne APENAS um JSON no formato:". Isso desencoraja a IA de adicionar preâmbulos ou explicações.
2.  **Esquema Rígido**: O JSON esperado é definido com chaves e valores permitidos (ex: `"categoria": "bug" | "enhancement" | "question"`), o que atua como uma validação de tipo para o modelo.
3.  **Tratamento de Saída**: No código, é realisado uma limpeza (`replace`) para remover possíveis blocos de código markdown (```json ... ```) que alguns modelos adicionam por padrão, garantindo que o `json.loads` receba uma string limpa.
4.  **Resumo Limitado**: Foi-se definido um limite de 100 caracteres para o resumo.


## Objetivo desse projeto:

Esse projeto tem como objetivo primario estudar e demonstrar o uso de uma IA para automação de uma tarefa do dia a dia, liberando o tempo de quem quer que esteja fazendo essa tarefa.

O escopo do projeto é limitado, mais a idea pode ser expandida para automatizar qualquer tarefa mais complicada que o projeto de detecção de anomalias em logs seria insuficiente. A escolha de rodar o projeto em CLI foi uma questão de tempo, mais implementar uma interface GUI é inteiramente possivel, até mesmo sem a modificação de nenhum codigo agora presente, apenas a adição de um novo script.

A IA escolhida foi o Gemini, por ter uma quantidade de tokens gratis quando se usa sua API e por eu ja ter trabalhado com os modelos do Google. Mais, com poucas modificações, qualquer IA pode ser usado "como ChatGPT ou Claude".
