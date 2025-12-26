import os
import faiss
import numpy as np
from logger import get_logger


class FaissDeduper:
    """
    Streaming-safe FAISS deduplicator.
    Handles:
    - inflight duplicates
    - historical duplicates
    - persistent index
    """

    def __init__(
        self,
        embedding_dim: int,
        index_path: str = "faiss_chunks.index",
        similarity_threshold: float = 0.95,
    ):
        self.embedding_dim = embedding_dim
        self.index_path = index_path
        self.similarity_threshold = similarity_threshold
        self.logger = get_logger(__name__)

        self.index = self._load_or_create_index()

    # -------------------------
    # Index lifecycle
    # -------------------------

    def _load_or_create_index(self) -> faiss.Index:
        """
        Load FAISS index if present, otherwise create a new one.
        Validates embedding dimension.
        """
        if os.path.exists(self.index_path):
            self.logger.info(f"Loading FAISS index from {self.index_path}")
            index = faiss.read_index(self.index_path)

            if index.d != self.embedding_dim:
                raise ValueError(
                    f"FAISS index dim mismatch: index={index.d}, expected={self.embedding_dim}"
                )

            return index

        self.logger.info(
            f"Creating new FAISS IndexFlatIP (dim={self.embedding_dim})"
        )
        index = faiss.IndexFlatIP(self.embedding_dim)
        return index

    def persist(self):
        """Persist FAISS index to disk."""
        faiss.write_index(self.index, self.index_path)
        self.logger.info(
            f"Persisted FAISS index ({self.index.ntotal} vectors)"
        )

    # -------------------------
    # Dedup logic
    # -------------------------

    def _prepare_embedding(self, embedding: np.ndarray) -> np.ndarray:
        """
        Normalize and reshape embedding for FAISS.
        """
        if embedding.ndim != 1:
            raise ValueError("Embedding must be 1D")

        if embedding.shape[0] != self.embedding_dim:
            raise ValueError(
                f"Embedding dim mismatch: got={embedding.shape[0]}, expected={self.embedding_dim}"
            )

        vec = embedding.astype("float32").reshape(1, -1)
        faiss.normalize_L2(vec)
        return vec

    def is_duplicate(self, embedding: np.ndarray) -> bool:
        """
        Check whether embedding is duplicate.
        """
        if self.index.ntotal == 0:
            return False

        vec = self._prepare_embedding(embedding)
        scores, _ = self.index.search(vec, k=1)

        similarity = float(scores[0][0])
        return similarity >= self.similarity_threshold

    def add(self, embedding: np.ndarray):
        """
        Add embedding to FAISS index.
        """
        vec = self._prepare_embedding(embedding)
        self.index.add(vec)
