import gc

import logger
from components.chunking import Chunking
from components.dedup import Dedupe
from ingestion.entities.embedder import Embedder
from components.faiss_dedup import FaissDeduper
from entities.ingestion_deps import IngestionDeps
from entities.ingestion_state import IngestionState
from components.vector_db import VectorDB
from ingestion.workflow.chunk_embedd_step import chunk_embedd_step
from ingestion.workflow.dedup_step import dedup_step
from ingestion.workflow.ingestion_step import ingestion_step
from ingestion.workflow.persist_step import persist_step
from ingestion.components.pipeline import Pipeline
from content.generator_builder import get_generators

logger = logger.get_logger(__name__)

def get_deps() -> IngestionDeps:

    deps = IngestionDeps()
    embedder = Embedder()
    deps.store = VectorDB()
    faiss_deduper = FaissDeduper(embedding_dim=384, similarity_threshold=0.95, index_path='../faiss_chunks.index')
    deps.dedupe = Dedupe(faiss_deduper=faiss_deduper)
    deps.chunking = Chunking(embedder=embedder)
    return deps

def run_workflow():

    pipe = Pipeline()
    deps = get_deps()

    steps = [
        ingestion_step,
        chunk_embedd_step,
        dedup_step,
        persist_step,
    ]

    for generator in get_generators():
        logger.info(f'started processing: {generator['gen'].__class__.__name__} with start id: {generator['st']} and end id: {generator['ed']}')

        state = IngestionState(deps=deps, generator=generator['gen'], start_id=generator['st'], end_id=generator['ed'])
        state = pipe.run(steps=steps, state=state)

        logger.info(f'completed processing: {generator['gen'].__class__.__name__} with start id: {generator['st']} and end id: {generator['ed']}')

        print(state.steps_ran)

        del state.qas
        del state.chunks
        del state.dedupe_chunks
        del state.steps_ran
        del state.errors
        gc.collect()


if __name__ == '__main__':
    run_workflow()


