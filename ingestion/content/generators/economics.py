from ingestion.content.generators.BaseGenerator import BaseGenerator

class Economics(BaseGenerator):

    def get_topic(self) -> str:
        return "economics"

    def get_subtopics(self) -> list[str]:
        return [
            "supply and demand", "market structures", "fiscal policy", "monetary policy",
            "international trade", "inflation", "unemployment", "economic growth",
            "price theory", "game theory"
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
        "market equilibrium challenge", "policy intervention problem", "trade balance scenario",
        "inflation control issue", "unemployment mitigation strategy", "economic growth analysis",
        "price fluctuation problem", "strategic interaction scenario", "monetary policy effectiveness", "fiscal deficit impact"
    ]

    openers = [
        "In practical economic analysis,",
        "From a macroeconomic perspective,",
        "During market evaluation exercises,",
        "Historically,",
        "When modeling supply-demand interactions,",
        "In policy-making contexts,"
    ]

    bridges = [
        "this rarely behaves as expected without considering behavioral and structural factors.",
        "issues often propagate through multiple sectors and time periods.",
        "problems often surface only under shocks or extreme market conditions.",
        "small deviations can drastically affect policy outcomes and equilibrium.",
        "what seems theoretically optimal can fail under real-world economic constraints."
    ]

    closers = [
        "which is why careful modeling, data analysis, and scenario planning are essential.",
        "and this insight usually emerges from repeated simulations and historical case studies.",
        "making it a recurring topic in economic research and policy education.",
        "and there is rarely a single universally correct intervention strategy.",
        "a lesson reinforced by real-world macroeconomic and microeconomic dynamics."
    ]

    middle_sentences = [
        "Supply and demand dynamics can be influenced by behavioral biases and external shocks.",
        "Market structures affect competition, pricing, and efficiency outcomes.",
        "Fiscal and monetary policies have lagged effects that complicate direct assessment.",
        "International trade involves exchange rates, tariffs, and comparative advantage considerations.",
        "Inflation and unemployment are interlinked through macroeconomic trade-offs.",
        "Game theory scenarios highlight strategic interdependence among economic agents."
      ]