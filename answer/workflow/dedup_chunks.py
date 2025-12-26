from typing import Tuple, Dict, Any, List
import numpy as np

from ingestion.entities.answer_state import AnswerState
from collections import defaultdict
from sklearn.metrics.pairwise import cosine_similarity

# pick best chunks for each qid
PER_QID_LIMIT = 2
ChunkRecord = Tuple[str, Dict[str, Any], float, np.ndarray]

def dedup_chunks(state: AnswerState):

    #group by qid
    grouped: dict[str, list[ChunkRecord]] = defaultdict(list)

    # group chunk hits
    for doc, meta, dist, emb in state.q_docs:
        grouped[meta["qid"]].append((doc, meta, dist, emb))

    # group QA hits (used only for routing, not dedup)
    # for doc, meta, dist, emb in state.qa_docs:
    #     grouped[meta["qid"]].append((doc, meta, dist, emb))

    merged_chunks: list[ChunkRecord] = []

    for qid, items in grouped.items():
        # split by embedding type
        chunk_items = [i for i in items if i[1].get("embedding_type") == "chunk"]
        #qa_items = [i for i in items if i[1].get("embedding_type") == "qa"]

        # sort chunks by distance
        chunk_items.sort(key=lambda x: x[2])
        merged_chunks.extend(chunk_items[:PER_QID_LIMIT])

        # # optionally keep best QA hit for reference
        # if qa_items:
        #     qa_items.sort(key=lambda x: x[2])
        #     state.best_qa_hits[qid] = qa_items[0]

    # semantic dedup only on chunks
    deduped_chunks = semantic_dedup(merged_chunks)

    # stable ordering for prompt construction
    state.deduped_chunks = sorted(
        deduped_chunks,
        key=lambda x: (
            x[2],  # distance
            x[1]["qid"],  # group stability
            x[1].get("chunk_index", 0)  # reading order
        )
    )

    return state

def semantic_dedup(
    chunks: List[ChunkRecord],
    threshold: float = 0.92
) -> List[ChunkRecord]:
    """
    Semantic deduplication using cosine similarity.
    Assumes all records are chunk embeddings.
    """

    if len(chunks) <= 1:
        return chunks

    embeddings = np.vstack([emb for _, _, _, emb in chunks])

    sim = cosine_similarity(embeddings)

    keep: list[ChunkRecord] = []
    removed: set[int] = set()

    for i in range(len(chunks)):
        if i in removed:
            continue

        keep.append(chunks[i])

        for j in range(i + 1, len(chunks)):
            if sim[i, j] >= threshold:
                removed.add(j)

    return keep
