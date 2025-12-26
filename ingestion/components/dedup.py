from typing import Any, Dict, Iterator
import numpy as np

from ingestion.components.faiss_dedup import FaissDeduper
from logger import get_logger

class Dedupe:
    """
    Streaming FAISS-based deduplication for chunk ingestion.
    """

    def __init__(self, faiss_deduper: FaissDeduper):
        self.logger = get_logger(__name__)
        self.faiss = faiss_deduper

    def deduplicate_chunks(
        self,
        chunks: Iterator[Dict[str, Any]],
    ) -> Iterator[Dict[str, Any]]:
        """
        Streaming dedup:
        - Checks each chunk against historical FAISS index
        - Yields only unique chunks
        """
        for chunk in chunks:
            embedding = np.array(chunk["embeddings"], dtype=np.float32)

            if embedding.ndim != 1:
                raise ValueError("Chunk embedding must be 1D vector")

            if self.faiss.is_duplicate(embedding):
                # self.logger.debug(
                #     f"Duplicate chunk skipped (qid={chunk['metadata']['qid']})"
                # )
                continue

            self.faiss.add(embedding)
            yield chunk

    def save(self):
        """
        Persist FAISS index to disk.
        Call once per batch or on shutdown.
        """
        self.faiss.persist()