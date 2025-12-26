from ingestion.content.generators.BaseGenerator import BaseGenerator

class DataEngineering(BaseGenerator):

    def get_topic(self) -> str:
        return "Data engineering"

    def get_subtopics(self) -> list[str]:
        return [
            "ETL pipeline", "data ingestion", "data transformation", "data warehouse",
            "data lake", "stream processing", "batch processing", "schema evolution",
            "data quality", "data validation"
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
        "Data transformation errors can propagate silently and affect downstream analytics.",
        "Batch and stream processing trade-offs often reveal latency and consistency issues.",
        "Schema evolution can break multiple dependent jobs unexpectedly.",
        "Data quality issues frequently emerge under high-volume ingestion scenarios.",
        "Validation failures often uncover overlooked edge cases in production pipelines.",
        "Monitoring and alerting are critical to detect early pipeline anomalies."
      ]

    question_intents = [
        "pipeline failure analysis",
        "data consistency challenge",
        "performance optimization scenario",
        "schema evolution reasoning",
        "real-time processing trade-off",
        "batch vs stream decision",
        "data validation edge case",
        "quality control failure",
        "scalability concern",
        "storage and retrieval efficiency"
    ]

    openers = [
        "In real-world data engineering pipelines,",
        "From a production data perspective,",
        "During ETL failures,",
        "Historically,",
        "When scaling data systems,",
        "In multi-source data integration,"
    ]

    bridges = [
        "this rarely occurs in isolation.",
        "the implications often propagate across systems.",
        "teams often notice this only after data discrepancies appear.",
        "small transformation choices can amplify errors downstream.",
        "what seems correct in staging can fail under production load."
    ]

    closers = [
        "which is why data engineers continually refine pipelines and monitoring.",
        "and this insight usually comes from operational experience.",
        "making it a recurring topic in postmortem and debugging sessions.",
        "and there is rarely a single universally correct approach.",
        "a lesson reinforced by repeated production incidents."
    ]