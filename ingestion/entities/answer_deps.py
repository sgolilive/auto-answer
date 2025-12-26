from typing import Optional

from ingestion.components.faiss_dedup import FaissDeduper
from ingestion.entities.embedder import Embedder
from ingestion.components.llm import LLM
from ingestion.components.vector_db import VectorDB


class AnswerDeps:
    vector_db: Optional[VectorDB] = None
    embedder: Optional[Embedder] = None
    llm: Optional[LLM] = None
    faiss_deduper: Optional[FaissDeduper] = None