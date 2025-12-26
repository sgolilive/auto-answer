from ingestion.entities.ingestion_state import IngestionState


def chunk_embedd_step(state: IngestionState) -> IngestionState:
    state.chunks = state.deps.chunking.chunk_answer_text(state.qas)
    return state
