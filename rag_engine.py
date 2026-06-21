from dataclasses import dataclass

from langchain_chroma import Chroma
from langchain_core.prompts import ChatPromptTemplate
from langchain_groq import ChatGroq
from langchain_huggingface import HuggingFaceEmbeddings

from config import (
    CHAT_MODEL,
    CHROMA_DIR,
    COLLECTION_NAME,
    EMBEDDING_MODEL,
    GROQ_API_KEY,
    MIN_RELEVANCE_SCORE,
    TOP_K,
)

PROMPT_TEMPLATE = """
Eres Ana, asistente técnico especializado en el manual SAP.

Reglas:
- Solo usa el contexto.
- No inventes información.
- Si no hay respuesta di:
"No encuentro esa informacion en el manual SAP consultado."

Contexto:
{context}

Pregunta:
{question}

Respuesta:
"""

@dataclass
class RagAnswer:
    answer: str
    pages: list[int]
    chunks: list[dict]


class ReglamentoRAG:

    def __init__(self):

        if not GROQ_API_KEY:
            raise RuntimeError("Falta GROQ_API_KEY en .env")

        self.embeddings = HuggingFaceEmbeddings(
            model_name=EMBEDDING_MODEL
        )

        self.vector_store = Chroma(
            persist_directory=str(CHROMA_DIR),
            embedding_function=self.embeddings,
            collection_name=COLLECTION_NAME,
        )

        self.llm = ChatGroq(
            api_key=GROQ_API_KEY,
            model=CHAT_MODEL,
            temperature=0.1,
        )

        self.prompt = ChatPromptTemplate.from_template(PROMPT_TEMPLATE)

    def ask(self, question: str) -> RagAnswer:

        question = question.strip()
        if not question:
            return RagAnswer("Escribe una pregunta.", [], [])

        results = self.vector_store.similarity_search_with_relevance_scores(
            question,
            k=TOP_K,
        )

        filtered = [
            (doc, score)
            for doc, score in results
            if score is None or score >= MIN_RELEVANCE_SCORE
        ]

        if not filtered:
            return RagAnswer(
                "No encuentro esa informacion en el manual SAP consultado.",
                [],
                [],
            )

        context = self._format_context(filtered)

        prompt = self.prompt.invoke({
            "context": context,
            "question": question
        })

        response = self.llm.invoke(prompt)

        return RagAnswer(
            response.content,
            self._extract_pages(filtered),
            self._serialize(filtered),
        )

    def _format_context(self, results):
        return "\n\n".join(doc.page_content for doc, _ in results)

    def _extract_pages(self, results):
        return list(set(
            self._get_page(doc.metadata)
            for doc, _ in results
            if self._get_page(doc.metadata) is not None
        ))

    def _get_page(self, metadata):
        page = metadata.get("page")
        return int(page) + 1 if page is not None else None

    def _serialize(self, results):
        return [
            {
                "page": self._get_page(doc.metadata),
                "content": doc.page_content,
                "score": float(score) if score else None,
            }
            for doc, score in results
        ]