from ingestion.entities.answer_state import AnswerState


def question_embedder_step(state: AnswerState) -> AnswerState:
    state.embeddings = state.deps.embedder.embed(state.question)
    return state