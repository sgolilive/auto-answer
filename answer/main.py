from answer.workflow.answer_step import answer_step
from answer.workflow.context_builder_step import build_context
from answer.workflow.dedup_chunks import dedup_chunks
from answer.workflow.embedder_step import question_embedder_step
from answer.workflow.prompt_builder_step import build_prompt
from answer.workflow.q_embedd_step import find_q_embedd_step
from answer.workflow.qa_embedd_step import find_qa_embedd_step
from ingestion.components.llm import LLM
from ingestion.components.pipeline import Pipeline
from ingestion.components.vector_db import VectorDB
from ingestion.entities.answer_deps import AnswerDeps
from ingestion.entities.answer_state import AnswerState
from ingestion.entities.embedder import Embedder


def get_deps():
    deps = AnswerDeps()
    deps.llm = LLM()
    deps.embedder = Embedder()
    deps.vector_db = VectorDB()
    return deps


def find_solution():
    steps = [question_embedder_step, find_q_embedd_step, dedup_chunks, build_context, build_prompt, answer_step]

    question = 'explain importance of function in the context of programming'

    state = AnswerState(deps=get_deps(), question=question)

    pipe = Pipeline()
    state = pipe.run(steps=steps, state=state)

    if not state.errors:
        print(state.answer)

if __name__ == '__main__':
    find_solution()