from ingestion.content.generators.BaseGenerator import BaseGenerator

class DataScienceAnalytics(BaseGenerator):

    def get_topic(self) -> str:
        return "Data Science and Analytics"

    def get_subtopics(self) -> list[str]:
        return [
            "exploratory data analysis (EDA)", "data visualization", "statistical modeling",
            "hypothesis testing", "A/B testing", "feature engineering",
            "data pipelines", "predictive modeling", "dashboard design", "data quality assessment"
        ]

    def get_sentence_pool(self) -> list[str]:
        pass

    def get_intro_options(self, subtopic: str) -> list[str]:
        pass

    def generate_question(self, subtopic: str) -> str:
        return super().generate_question(subtopic)

    def generate_answer(self, subtopic: str) -> str:
        return super().generate_answer(subtopic)

    question_intents = [
        "data-driven decision scenario", "statistical anomaly detection", "model performance evaluation",
        "feature selection challenge", "visualization misinterpretation", "A/B testing edge case",
        "data pipeline failure", "predictive modeling trade-off", "dashboard design issue", "data quality problem"
    ]

    openers = [
        "In practical data science scenarios,",
        "From an analytics perspective,",
        "During exploratory analysis exercises,",
        "Historically,",
        "When designing data pipelines,",
        "In real-world decision-making contexts,"
    ]

    bridges = [
        "this rarely behaves as expected without careful preprocessing.",
        "issues often propagate through multiple stages of analysis.",
        "problems often surface only when handling large, heterogeneous datasets.",
        "small mistakes in feature engineering can lead to misleading conclusions.",
        "what seems obvious in theory can fail during real-world experimentation."
    ]

    closers = [
        "which is why rigorous validation and testing are essential.",
        "and this insight usually emerges from repeated modeling and analysis iterations.",
        "making it a recurring topic in data science practice and education.",
        "and there is rarely a single universally correct solution.",
        "a lesson reinforced by real-world analytics deployments and experiments."
    ]

    middle_sentences = [
        "Incorrect feature engineering can introduce bias and reduce model accuracy.",
        "A/B testing misconfigurations can lead to false conclusions about user behavior.",
        "Data visualization may mislead stakeholders if scales or aggregations are inappropriate.",
        "Pipeline failures can corrupt downstream analyses if not properly monitored.",
        "Predictive models may overfit or underfit depending on data quality and preprocessing.",
        "Hypothesis testing requires careful consideration of assumptions and statistical significance."
      ]