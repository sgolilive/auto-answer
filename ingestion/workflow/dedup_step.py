from ingestion.entities.ingestion_state import IngestionState


def dedup_step(state: IngestionState) -> IngestionState:
    state.dedupe_chunks = state.deps.dedupe.deduplicate_chunks(state.chunks)
    return state