from answer.workflow.find_embedd_step import find_embedd_step
from ingestion.entities.answer_state import AnswerState

def find_qa_embedd_step(state: AnswerState) -> AnswerState:
    state.qa_docs = find_embedd_step(state, filters={'embedding_type': 'qa'})
    return state