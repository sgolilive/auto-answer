from ingestion.content.generators.BaseGenerator import BaseGenerator

class LogicalReasoning(BaseGenerator):

    def get_topic(self) -> str:
        return "logical reasoning"

    def get_subtopics(self) -> list[str]:
        return [
        "deductive reasoning", "inductive reasoning", "logical fallacy",
        "cause and effect", "syllogism", "pattern recognition",
        "analogy", "critical thinking", "problem solving"
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
        "complex scenario analysis",
        "fallacy identification challenge",
        "pattern recognition under ambiguity",
        "cause-effect relationship reasoning",
        "syllogism evaluation",
        "real-world problem-solving scenario",
        "decision-making edge case",
        "critical thinking assessment",
        "analogy mapping challenge",
        "logical reasoning failure analysis"
    ]

    openers = [
        "In practical reasoning scenarios,",
        "From a critical thinking perspective,",
        "During problem-solving exercises,",
        "Historically,",
        "When evaluating logical arguments,",
        "In complex decision-making contexts,"
    ]

    bridges = [
        "this rarely behaves as expected without careful analysis.",
        "effects often propagate through multiple assumptions.",
        "errors often surface only under ambiguous conditions.",
        "small misinterpretations can lead to incorrect conclusions.",
        "what seems straightforward may have hidden subtleties."
    ]

    closers = [
        "which is why rigorous reasoning and verification are essential.",
        "and this insight usually emerges from repeated practice and reflection.",
        "making it a recurring topic in logic and reasoning studies.",
        "and there is rarely a single universally correct answer.",
        "a lesson reinforced by extensive evaluation of real-world scenarios."
    ]

    middle_sentences = [
        "Logical fallacies can distort interpretation and lead to invalid conclusions.",
        "Pattern recognition sometimes fails under ambiguous or incomplete data.",
        "Cause-effect reasoning requires careful analysis of confounding factors.",
        "Syllogism exercises often expose subtle gaps in assumptions.",
        "Analogies can mislead if underlying structures are not properly understood.",
        "Critical thinking often demands iterative evaluation of multiple perspectives."
      ]
