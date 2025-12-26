from ingestion.entities.answer_state import AnswerState

def build_context(state: AnswerState, max_tokens=512) -> AnswerState:
    reserved_for_question = 120
    available = max_tokens - reserved_for_question

    context_chunks = []
    used = 0

    for i, (doc, meta, dist, emb) in enumerate(state.deduped_chunks):
        prefix = f"Source {i + 1}:\n"
        text = prefix + doc + "\n\n"

        token_len = len(state.deps.llm.tokenizer.encode(text, add_special_tokens=False))

        if used + token_len > available:
            break

        context_chunks.append(text)
        used += token_len

    state.context = "".join(context_chunks)
    return state