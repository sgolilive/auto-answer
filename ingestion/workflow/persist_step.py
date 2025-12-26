from ingestion.entities.ingestion_state import IngestionState

def persist_step(state: IngestionState) -> IngestionState:
    state.deps.store.upsert(state.dedupe_chunks)
    state.deps.dedupe.save()
    return state