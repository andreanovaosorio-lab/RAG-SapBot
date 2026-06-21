from langchain_chroma import Chroma
from langchain_community.document_loaders import PyPDFLoader
from langchain_community.embeddings import HuggingFaceEmbeddings
from langchain_text_splitters import RecursiveCharacterTextSplitter

from config import (
    CHROMA_DIR,
    CHUNK_SIZE,
    CHUNK_OVERLAP,
    COLLECTION_NAME,
    EMBEDDING_MODEL,
    PDF_PATH,
)


def build_vector_store():

    if not PDF_PATH.exists():
        raise FileNotFoundError(f"No se encontró el PDF: {PDF_PATH}")

    # 1. cargar PDF
    loader = PyPDFLoader(str(PDF_PATH))
    pages = loader.load()

    # 2. dividir texto
    splitter = RecursiveCharacterTextSplitter(
        chunk_size=CHUNK_SIZE,
        chunk_overlap=CHUNK_OVERLAP,
    )

    chunks = splitter.split_documents(pages)

    # 3. embeddings LOCALES (sin API)
    embeddings = HuggingFaceEmbeddings(
        model_name=EMBEDDING_MODEL
    )

    # 4. guardar en Chroma
    Chroma.from_documents(
        documents=chunks,
        embedding=embeddings,
        persist_directory=str(CHROMA_DIR),
        collection_name=COLLECTION_NAME,
    )

    print("✔ Indexación completada")
    print(f"Paginas: {len(pages)}")
    print(f"Chunks: {len(chunks)}")


if __name__ == "__main__":
    build_vector_store()