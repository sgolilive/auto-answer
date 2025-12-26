from ingestion.content.generators.BaseGenerator import BaseGenerator

class Database(BaseGenerator):

    def get_topic(self) -> str:
        return "Database"

    def get_subtopics(self) -> list[str]:
        return [
            "relational database", "NoSQL database", "SQL", "indexing",
            "transactions", "ACID properties", "normalization", "denormalization",
            "replication", "sharding", "data consistency", "CAP theorem"
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
        "Theoretical understanding helps, but real workloads reveal unexpected behavior.",
        "Small design shortcuts can have amplified consequences at scale.",
        "Replication and sharding choices interact in subtle ways affecting consistency.",
        "Query performance issues often cascade across the system.",
        "Operational monitoring usually uncovers hidden bottlenecks.",
        "Failover strategies often highlight unanticipated edge cases."
      ]

    question_intents = [
        "production failure analysis",
        "architecture trade-off evaluation",
        "performance optimization perspective",
        "scalability concern discussion",
        "real-world debugging scenario",
        "consistency vs availability reasoning",
        "historical evolution explanation",
        "misconception clarification",
        "query optimization scenario",
        "replication and backup implication"
    ]

    openers = [
        "In large-scale database systems,",
        "When operating under high load,",
        "From a system design perspective,",
        "Historically,",
        "During production incidents,",
        "In multi-region deployments,"
    ]

    bridges = [
        "this rarely occurs in isolation.",
        "the effects often surface indirectly.",
        "teams often only notice this after replication delays become visible.",
        "complex queries can amplify hidden assumptions.",
        "what seems correct in theory can fail under real load."
    ]

    closers = [
        "which is why DBAs continuously refine strategies.",
        "and this usually becomes apparent during operational monitoring.",
        "making it a recurring topic in postmortem analysis.",
        "and this trade-off rarely has a universally correct solution.",
        "a lesson reinforced by repeated scaling experiments."
    ]