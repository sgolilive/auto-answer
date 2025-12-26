from ingestion.content.generators.BaseGenerator import BaseGenerator

class FinanceInvestment(BaseGenerator):

    def get_topic(self) -> str:
        return "financial and investment"

    def get_subtopics(self) -> list[str]:
        return [
            "equity markets", "bond markets", "mutual funds", "derivatives", "risk management",
            "portfolio optimization", "financial modeling", "corporate finance", "valuation techniques",
            "behavioral finance"
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
        "investment decision challenge", "risk assessment problem", "portfolio allocation scenario",
        "valuation modeling issue", "derivatives pricing problem", "market behavior analysis",
        "financial strategy evaluation", "regulatory compliance difficulty", "corporate finance decision", "behavioral bias consideration"
    ]

    openers = [
        "In practical finance exercises,",
        "From an investment perspective,",
        "During portfolio management sessions,",
        "Historically,",
        "When analyzing market and corporate data,",
        "In risk and strategy evaluation contexts,"
    ]

    bridges = [
        "this rarely behaves as expected without careful quantitative and qualitative analysis.",
        "issues often propagate through multiple market instruments and interdependencies.",
        "problems often surface only under volatile or stressed market conditions.",
        "small changes in assumptions can drastically affect risk and return outcomes.",
        "what seems profitable theoretically can fail under behavioral or operational constraints."
    ]

    closers = [
        "which is why rigorous modeling, stress-testing, and strategy refinement are essential.",
        "and this insight usually emerges from historical data analysis and scenario planning.",
        "making it a recurring topic in finance education and professional practice.",
        "and there is rarely a single universally optimal investment strategy.",
        "a lesson reinforced by market cycles and investment outcomes over time."
    ]

    middle_sentences = [
        "Equity markets require analysis of company fundamentals, market trends, and valuation metrics.",
        "Bond markets involve interest rate risk, credit quality, and duration considerations.",
        "Mutual funds and derivatives require understanding of portfolio composition and hedging strategies.",
        "Risk management involves identifying, quantifying, and mitigating financial and operational risks.",
        "Portfolio optimization balances risk, return, and investor objectives across asset classes.",
        "Behavioral finance studies how psychological biases affect market decisions and asset pricing."
      ]