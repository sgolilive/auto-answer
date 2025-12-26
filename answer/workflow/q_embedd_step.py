from answer.workflow.find_embedd_step import find_embedd_step
from ingestion.entities.answer_state import AnswerState

def find_q_embedd_step(state: AnswerState) -> AnswerState:
    state.q_docs = find_embedd_step(state, filters={'embedding_type': 'chunk'})
    return state