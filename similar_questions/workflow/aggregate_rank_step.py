from ingestion.entities.answer_state import SimilarQuestionState


def aggregate_rank_step(state: SimilarQuestionState) -> SimilarQuestionState:
    qid_scores = []

    for doc, meta, dist, _ in state.qa_docs:
        qid_scores.append({
            'qid': meta["qid"],
            'question': doc,
            'confidence': round(1 - dist, 2)
        })

    state.qid_scores = qid_scores

    return state