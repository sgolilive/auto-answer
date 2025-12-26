from ingestion.entities.ingestion_state import IngestionState

def ingestion_step(state: IngestionState) -> IngestionState:
    state.qas = state.generator.get_qas(state.start_id, state.end_id)
    return state