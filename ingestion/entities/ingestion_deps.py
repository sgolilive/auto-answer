from typing import Optional

from ingestion.components.chunking import Chunking
from ingestion.components.dedup import Dedupe
from ingestion.components.vector_db import VectorDB
from dataclasses import dataclass


@dataclass
class IngestionDeps:
    chunking: Optional[Chunking] = None
    dedupe: Optional[Dedupe] = None
    store: Optional[VectorDB] = None