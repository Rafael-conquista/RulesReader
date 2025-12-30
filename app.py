import os
import streamlit as st

from langchain_community.document_loaders import PyPDFLoader, TextLoader
from langchain_openai import ChatOpenAI
from langchain_core.messages import HumanMessage

BASE_DIR = "games"
os.makedirs(BASE_DIR, exist_ok=True)

st.set_page_config(page_title="Board Game Manual AI", layout="centered")

st.title("🎲 Board Game Manual AI")
st.caption("Responde usando TODO o manual como fonte")


game_name = st.text_input("Nome do jogo")

uploaded_file = st.file_uploader(
    "Upload do manual (PDF ou TXT)",
    type=["pdf", "txt"]
)

question = st.text_input("Pergunta sobre o jogo")


def game_path(name: str) -> str:
    return os.path.join(BASE_DIR, name)


def manual_path(name: str) -> str:
    return os.path.join(game_path(name), "manual.txt")


def manual_exists(name: str) -> bool:
    return os.path.exists(manual_path(name))


if uploaded_file and game_name:
    if st.button("📚 Processar manual"):
        path = game_path(game_name)
        os.makedirs(path, exist_ok=True)

        file_path = os.path.join(path, uploaded_file.name)
        with open(file_path, "wb") as f:
            f.write(uploaded_file.read())

        if file_path.lower().endswith(".pdf"):
            loader = PyPDFLoader(file_path)
        else:
            loader = TextLoader(file_path, encoding="utf-8")

        docs = loader.load()

        full_text = "\n\n".join(d.page_content for d in docs)

        full_text = (
            full_text
            .replace("\n", " ")
            .replace("  ", " ")
        )

        with open(manual_path(game_name), "w", encoding="utf-8") as f:
            f.write(full_text)

        st.success("Manual carregado com sucesso!")


if question and game_name:
    if not manual_exists(game_name):
        st.error("Manual não encontrado. Faça o upload primeiro.")
    else:
        with st.spinner("Consultando manual completo..."):
            with open(manual_path(game_name), "r", encoding="utf-8") as f:
                manual_text = f.read()

            llm = ChatOpenAI(
                openai_api_base="http://localhost:1234/v1",
                openai_api_key="lm-studio",
                model_name="mistral-7b-instruct",
                temperature=0
            )

            prompt = f"""
Você é um analisador estrito de regras de jogos de tabuleiro.

⚠️ REGRAS ABSOLUTAS:
- NÃO use conhecimento externo
- NÃO faça inferências
- NÃO associe nomes conhecidos fora do texto
- SÓ responda se a informação estiver EXPLICITAMENTE descrita no manual

Antes de responder, verifique:
1. O manual menciona exatamente o que está sendo perguntado?
2. Existe um trecho que prova a resposta?

Se NÃO existir prova textual clara, responda EXATAMENTE:
"O manual não especifica essa informação."

MANUAL COMPLETO:
{manual_text}

PERGUNTA:
{question}

Responda apenas se houver evidência explícita no manual.

"""

            response = llm.invoke([
                HumanMessage(content=prompt)
            ])

            st.markdown("### 📖 Resposta")
            st.write(response.content)
