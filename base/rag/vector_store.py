from pathlib import Path
from django.conf import settings
from langchain_chroma import Chroma

from .embeddings import get_embeddings


CHROMA_PATH = Path(settings.BASE_DIR) / "chroma_db"

COLLECTION_NAME = "resume_knowledge_langchain"


def get_vector_store():
    return Chroma(
        collection_name=COLLECTION_NAME,
        embedding_function=get_embeddings(),
        persist_directory=str(CHROMA_PATH),
        collection_metadata={
            "hnsw:space": "cosine"
        }
    )



