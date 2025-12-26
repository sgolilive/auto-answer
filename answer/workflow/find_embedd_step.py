from ingestion.entities.answer_state import AnswerState

def find_embedd_step(state: AnswerState, filters=None) -> list:
    results = state.deps.vector_db.query(
        query_embedding=state.embeddings,
        top_k=20,
        include=['documents', 'metadatas', 'distances', 'embeddings'],
        filters=filters
    )

    return [(doc, meta, dist, emb) for doc, meta, dist, emb in zip(
        results['documents'][0],
        results['metadatas'][0],
        results['distances'][0],
        results['embeddings'][0])]
