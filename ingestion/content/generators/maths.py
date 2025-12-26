from ingestion.content.generators.BaseGenerator import BaseGenerator

class Mathematics(BaseGenerator):

    def get_topic(self) -> str:
        return "mathematics"

    def get_subtopics(self) -> list[str]:
        return [
            "prime number", "factorial", "linear equation", "quadratic equation",
            "matrix", "determinant", "probability", "permutation", "combination",
            "mean", "median", "mode", "standard deviation", "variance"
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
        "real-world application problem",
        "complex problem solving",
        "probability analysis scenario",
        "matrix computation challenge",
        "optimization reasoning",
        "statistical inference edge case",
        "pattern recognition challenge",
        "algebraic manipulation scenario",
        "combinatorial reasoning problem",
        "error analysis in calculations"
    ]

    openers = [
        "In practical applications,",
        "When solving complex problems,",
        "From a mathematical modeling perspective,",
        "Historically,",
        "During real-world computations,",
        "In statistical analysis,"
    ]

    bridges = [
        "this rarely works as expected without careful reasoning.",
        "the effects often propagate across multiple steps.",
        "teams often notice mistakes only after verification.",
        "small miscalculations can amplify errors downstream.",
        "what seems simple can have unexpected subtleties in practice."
    ]

    closers = [
        "which is why careful analysis and verification are essential.",
        "and this insight usually comes from repeated problem solving.",
        "making it a recurring topic in mathematical exploration.",
        "and there is rarely a single universally correct approach.",
        "a lesson reinforced by multiple calculation scenarios."
    ]

    middle_sentences = [
        "Calculations often require careful handling of edge cases and constraints.",
        "Applying formulas mechanically may lead to subtle mistakes in results.",
        "Statistical and combinatorial reasoning frequently uncovers unexpected patterns.",
        "Matrices and determinants often interact in non-trivial ways in higher dimensions.",
        "Algebraic manipulation errors can propagate and amplify in sequences of calculations.",
        "Probability problems may have counter-intuitive outcomes if assumptions are overlooked."
      ]
