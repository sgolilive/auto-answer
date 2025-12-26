from ingestion.content.generators.BaseGenerator import BaseGenerator

class Finance(BaseGenerator):

    def get_topic(self) -> str:
        return "Finance"

    def get_subtopics(self) -> list[str]:
        return [
            "inflation", "deflation", "simple interest", "compound interest",
            "time value of money", "stock", "bond", "mutual fund",
            "market capitalization", "dividend", "risk", "return",
            "diversification", "supply and demand",
            "stock markets", "bonds", "derivatives", "portfolio management",
            "risk-return analysis", "diversification", "behavioral finance",
            "valuation techniques", "financial modeling", "fintech applications"
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
        "investment decision analysis",
        "risk-return trade-off evaluation",
        "portfolio optimization scenario",
        "market fluctuation reasoning",
        "financial modeling edge case",
        "interest calculation challenge",
        "capital allocation decision",
        "economic trend impact analysis",
        "asset correlation consideration",
        "real-world investment failure scenario",
        "risk assessment challenge", "investment allocation scenario", "market volatility problem",
        "valuation accuracy issue", "derivative pricing scenario", "portfolio optimization challenge",
        "financial modeling complexity", "behavioral bias mitigation", "regulatory compliance concern", "fintech integration problem"
    ]

    openers = [
        "In practical financial scenarios,",
        "From an investment strategy perspective,",
        "During market volatility,",
        "Historically,",
        "When managing portfolios,",
        "In real-world economic contexts,",
        "In practical finance scenarios,",
        "From an investment management perspective,",
        "During portfolio construction exercises,",
        "Historically,",
        "When analyzing market trends,",
        "In risk assessment contexts,"
    ]

    bridges = [
        "this rarely behaves as expected without careful modeling.",
        "the effects often propagate across multiple assets.",
        "analysts often notice issues only after market shifts.",
        "small allocation decisions can amplify portfolio risk.",
        "what seems safe in theory can fail under actual market conditions.",
        "unexpected fluctuations can have cascading effects on returns and risk.",
        "issues often propagate across asset classes and financial instruments.",
        "problems often surface only under extreme market conditions or stress scenarios.",
        "small errors in valuation can dramatically affect investment decisions.",
        "what seems optimal in theory may fail under real-world constraints."
    ]

    closers = [
        "which is why financial planners continually refine models and strategies.",
        "and this insight usually emerges from repeated market observations.",
        "making it a recurring topic in investment postmortems.",
        "and there is rarely a single universally correct approach.",
        "a lesson reinforced by repeated market fluctuations.",
        "which is why rigorous modeling, diversification, and risk management are essential.",
        "and this insight usually emerges from repeated simulations and historical analysis.",
        "making it a recurring topic in finance and investment studies.",
        "and there is rarely a single universally optimal strategy.",
        "a lesson reinforced by real-world market dynamics and investor behavior."
    ]

    middle_sentences = [
        "Risk-return trade-offs are rarely straightforward in real markets.",
        "Interest calculations can impact long-term investment strategies significantly.",
        "Portfolio diversification sometimes uncovers unexpected correlations.",
        "Market capitalization and liquidity can influence asset volatility.",
        "Economic trends may affect expected returns in non-intuitive ways.",
        "Dividend policies can interact with taxation and reinvestment strategies unexpectedly.",
        "Diversification reduces unsystematic risk but cannot eliminate market-wide fluctuations.",
        "Behavioral biases such as overconfidence or loss aversion can distort decision-making.",
        "Portfolio optimization requires balancing risk, return, and liquidity constraints.",
        "Derivative instruments are complex and sensitive to underlying market assumptions.",
        "Financial modeling relies on assumptions that may not hold in extreme conditions.",
        "Regulatory changes can impact investment strategies and compliance requirements."
      ]