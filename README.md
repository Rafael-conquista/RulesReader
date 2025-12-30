RulesReader é um agente de IA local para responder perguntas sobre manuais de jogos de tabuleiro, utilizando exclusivamente o texto do manual como fonte de verdade.

Este projeto prioriza correção e fidelidade às regras, mesmo que isso signifique respostas mais restritivas ou “manual não especifica”.

✨ Objetivo do Projeto

Permitir que o usuário:

Faça upload do manual oficial de um jogo de tabuleiro (PDF ou TXT)

Faça perguntas em linguagem natural

Receba respostas baseadas apenas no conteúdo do manual

Evite respostas inventadas, inferências ou conhecimento externo

📌 Ideal para:

Jogos como Santorini, Root, Terraforming Mars, Catan, etc.

Verificação rápida de regras

Evitar discussões na mesa de jogo 😄

⚠️ Filosofia Importante

Se a informação não estiver explicitamente descrita no manual, o sistema NÃO responde.

Isso é intencional.

O projeto foi desenhado para reduzir alucinação, mesmo que isso torne o agente menos “criativo”.

🧠 Abordagem Técnica
❌ O que o projeto NÃO usa

Não usa RAG com embeddings

Não usa FAISS

Não usa chunking

Não tenta “adivinhar” regras

✅ O que o projeto usa

Manual completo enviado como contexto

LLM local via LM Studio

Prompt estrito que proíbe inferências

Temperatura 0 (determinístico)

Essa abordagem é mais lenta, porém muito mais confiável para manuais pequenos e médios.

🏗️ Arquitetura
Usuário
 ├─ Upload do manual (PDF/TXT)
 ├─ Pergunta em linguagem natural
 └─ Streamlit UI
       ↓
Manual completo (texto puro)
       ↓
Prompt estrito
       ↓
LLM local (LM Studio)
       ↓
Resposta baseada no manual

🖥️ Interface

Aplicação web simples usando Streamlit

Campo para:

Nome do jogo

Upload do manual

Pergunta sobre regras

Exibe apenas a resposta final

📦 Requisitos

Python 3.10+

LM Studio rodando localmente

Um modelo compatível com OpenAI API (ex: mistral-7b-instruct)

📚 Dependências
pip install streamlit langchain langchain-community langchain-openai pypdf

▶️ Como Executar
1️⃣ Inicie o LM Studio

Abra o LM Studio

Carregue um modelo (ex: mistral-7b-instruct)

Ative o OpenAI-compatible API Server

Normalmente disponível em:

http://localhost:1234/v1

2️⃣ Execute a aplicação
python -m streamlit run .\app.py


Acesse no navegador:

http://localhost:8501

📝 Como Usar

Digite o nome do jogo

Faça upload do manual (PDF ou TXT)

Clique em “Processar manual”

Faça perguntas sobre o jogo

Exemplos de perguntas válidas:

“Quantos jogadores podem jogar?”

“Quais são as condições de vitória?”

“Qual é o poder do deus Zeus segundo o manual?”

Exemplos de perguntas problemáticas:

“O que a carta número 30 faz?”

“Qual é a melhor estratégia?”

“Quem é mais forte, Zeus ou Atena?”

➡️ Essas podem resultar em:

“O manual não especifica essa informação.”

E isso é o comportamento esperado.

❌ Limitações Conhecidas

Manuais muito grandes podem ultrapassar o limite de contexto do modelo

PDFs escaneados (imagem) não funcionam sem OCR

Não interpreta layout visual (tabelas, ícones, colunas)

Não resolve ambiguidades do próprio manual

🛡️ Por que não usar RAG?

RAG genérico com embeddings:

Fragmenta regras

Perde exceções

Falha com nomes próprios

Introduz respostas incorretas

Este projeto opta por:

Confiabilidade > performance

🚀 Possíveis Evoluções

Modo híbrido (manual inteiro + fallback)

Citação literal de trechos do manual

OCR para PDFs escaneados

Conversão PDF → Markdown

Suporte a múltiplos manuais por jogo

API REST

🤝 Contribuições

Contribuições são bem-vindas — especialmente:

Melhorias no prompt

Suporte a manuais maiores

Melhor pré-processamento de PDF

📌 Conclusão

Este projeto não tenta ser inteligente.
Ele tenta ser correto.

Se você quer um agente que:

Não inventa regras

Não “chuta”

Não mistura conhecimento externo

👉 Esse projeto é para você.
