from ingestion.entities.answer_state import AnswerState


def build_prompt(state: AnswerState) -> AnswerState:
    state.prompt = f'''
            You are a helpful assistant.
            
            Use the following sources to answer the question.
            If the answer cannot be found, say so clearly.

            context: {state.context}
            question: {state.question}
            answer:
            '''.strip()

    return state