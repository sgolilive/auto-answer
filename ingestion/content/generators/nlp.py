from ingestion.content.generators.BaseGenerator import BaseGenerator

class LLMNLP(BaseGenerator):

    def get_topic(self) -> str:
        return "LLM and NLP"

    def get_subtopics(self) -> list[str]:
        return [
            "large language model", "tokenization", "embeddings", "vector database",
            "semantic search", "retrieval augmented generation", "prompt engineering",
            "context window", "hallucination", "temperature", "fine tuning",
            "instruction tuning", "agent architecture"
        ]

    def get_sentence_pool(self) -> list[str]:
        pass

    def get_intro_options(self, subtopic: str) -> list[str]:
        pass

    def generate_question(self, subtopic: str) -> str:
        return super().generate_question(subtopic)

    def generate_answer(self, subtopic: str) -> str:
        return super().generate_answer(subtopic)

    middle_sentences = [
        "Outputs can vary significantly depending on prompt phrasing and context.",
        "Vector database retrieval sometimes returns semantically close but irrelevant items.",
        "Fine-tuning may improve accuracy but risks overfitting on small datasets.",
        "Hallucinations often occur when context windows are insufficient for reasoning.",
        "Agent pipelines can amplify errors if intermediate steps are not validated.",
        "Semantic search ranking sometimes conflicts with actual relevance in RAG."
      ]

    question_intents = [
        "model hallucination analysis",
        "retrieval performance evaluation",
        "prompt optimization scenario",
        "context window constraint reasoning",
        "semantic search debugging",
        "fine-tuning trade-off evaluation",
        "instruction tuning edge case",
        "agent behavior analysis",
        "deployment performance challenge",
        "real-world RAG failure scenario"
    ]

    openers = [
        "In real-world NLP systems,",
        "From a language model engineering perspective,",
        "During RAG deployment,",
        "Historically,",
        "In production scenarios,",
        "When integrating LLMs with downstream tasks,"
    ]

    bridges = [
        "this rarely occurs in isolation.",
        "the implications often surface indirectly across components.",
        "teams frequently notice issues only under full-scale queries.",
        "small prompt design choices can amplify unexpected outputs.",
        "what seems correct in testing can fail under production load."
    ]

    closers = [
        "which is why engineers continually refine prompt and retrieval pipelines.",
        "and this insight usually emerges from operational experience.",
        "making it a recurring topic in postmortem analysis and RAG evaluation.",
        "and there is rarely a single correct approach.",
        "a lesson reinforced by repeated retrieval and generation failures."
    ]
