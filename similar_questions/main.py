from answer.workflow.embedder_step import question_embedder_step
from answer.workflow.qa_embedd_step import find_qa_embedd_step
from ingestion.components.pipeline import Pipeline
from ingestion.components.vector_db import VectorDB
from ingestion.entities.answer_state import SimilarQuestionState, SimilarQuestionDeps
from ingestion.entities.embedder import Embedder
from similar_questions.workflow.aggregate_rank_step import aggregate_rank_step

def get_deps():
    deps = SimilarQuestionDeps()
    deps.embedder = Embedder()
    deps.vector_db = VectorDB()
    return deps

def search_similar_question():

    steps = [question_embedder_step, find_qa_embedd_step, aggregate_rank_step]
    question = 'explain importance of function in the context of programming'
    state = SimilarQuestionState(deps=get_deps(), question=question)

    pipe = Pipeline()
    pipe.run(steps=steps, state=state)

    for q in state.qid_scores:
        print(f'id: {q["qid"]}, question:{q['question']} , confidence: {q["confidence"]}')


if __name__ == '__main__':
    search_similar_question()