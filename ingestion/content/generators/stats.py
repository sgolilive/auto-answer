from ingestion.content.generators.BaseGenerator import BaseGenerator

class AdvancedMathematics(BaseGenerator):

    def get_topic(self) -> str:
        return "advanced mathematics and statistics"

    def get_subtopics(self) -> list[str]:
        return [
            "linear algebra", "calculus", "probability theory", "statistical inference",
            "matrix analysis", "optimization", "combinatorics", "graph theory",
            "time series analysis", "stochastic processes"
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
        "Linear algebra challenges often involve vector space properties, eigenvalues, and transformations.",
        "Calculus and optimization require careful handling of derivatives, integrals, and constraints.",
        "Probability theory involves managing uncertainty, conditional events, and distributions.",
        "Statistical inference requires assumptions about data, estimators, and hypothesis testing.",
        "Combinatorics and graph theory explore enumeration, connectivity, and discrete structures.",
        "Time series and stochastic processes require modeling temporal dependencies and randomness."
      ]

    question_intents = [
        "problem-solving challenge", "proof verification problem", "data analysis scenario",
        "statistical modeling issue", "optimization complexity problem", "combinatorial enumeration difficulty",
        "matrix computation challenge", "graph connectivity analysis", "time series forecasting issue", "stochastic simulation problem"
    ]

    openers = [
        "In practical mathematics and statistics exercises,",
        "From a theoretical and applied perspective,",
        "During advanced problem-solving sessions,",
        "Historically,",
        "When analyzing complex mathematical models,",
        "In statistical modeling and inference contexts,"
    ]

    bridges = [
        "this rarely behaves as expected without rigorous reasoning and verification.",
        "issues often propagate through multiple steps or assumptions in derivations.",
        "problems often surface only when edge cases or constraints are considered.",
        "small errors in computation or logic can drastically affect results.",
        "what seems straightforward mathematically can fail under real-world data complexity."
    ]

    closers = [
        "which is why meticulous derivation, validation, and numerical experimentation are essential.",
        "and this insight usually emerges from detailed proofs, simulations, and analytical checks.",
        "making it a recurring topic in advanced mathematics and statistics education.",
        "and there is rarely a single universally optimal solution for complex problems.",
        "a lesson reinforced by real-world modeling, computation, and statistical analysis."
    ]