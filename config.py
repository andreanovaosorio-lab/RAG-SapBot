from pathlib import Path
import os
from dotenv import load_dotenv

load_dotenv()

BASE_DIR = Path(__file__).resolve().parent

PDF_PATH = BASE_DIR / "pdf" / "TS460_2_ES_Col23.pdf"
CHROMA_DIR = BASE_DIR / "chromadb"
COLLECTION_NAME = "sap_ts460"

# GROQ (LLM)
GROQ_API_KEY = os.getenv("GROQ_API_KEY")

# MODELO LLM
CHAT_MODEL = os.getenv("CHAT_MODEL", "llama3-8b-8192")

#  EMBEDDINGS (locales)
EMBEDDING_MODEL = os.getenv(
    "EMBEDDING_MODEL",
    "sentence-transformers/all-MiniLM-L6-v2"
)

CHUNK_SIZE = int(os.getenv("CHUNK_SIZE", "900"))
CHUNK_OVERLAP = int(os.getenv("CHUNK_OVERLAP", "120"))
TOP_K = int(os.getenv("TOP_K", "6"))
MIN_RELEVANCE_SCORE = float(os.getenv("MIN_RELEVANCE_SCORE", "0.25"))