from ingestion.entities.answer_state import AnswerState


def answer_step(state: AnswerState) -> AnswerState:
    state.answer = state.deps.llm.generate_answer(state.prompt)
    return state

