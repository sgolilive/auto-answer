from ingestion.content.generators.BaseGenerator import BaseGenerator


class BlackChain(BaseGenerator):

    def get_topic(self) -> str:
        return "Black Chain and Web3"

    def get_subtopics(self) -> list[str]:
        return [
            "smart contracts", "consensus mechanisms", "DeFi protocols", "NFT marketplaces",
            "tokens and cryptocurrencies", "gas fees and transaction costs", "wallet security",
            "decentralized governance", "layer 2 scaling solutions", "oracles and data feeds"
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
        "smart contract vulnerability scenario", "consensus failure analysis",
        "DeFi protocol risk assessment", "NFT marketplace transaction issue",
        "token valuation challenge", "gas fee optimization problem",
        "wallet compromise scenario", "DAO governance decision analysis",
        "layer 2 scaling limitation", "oracle data manipulation scenario"
    ]

    openers = [
        "In real-world blockchain and Web3 scenarios,",
        "From a smart contract security perspective,",
        "During DeFi and NFT protocol exercises,",
        "Historically,",
        "When managing decentralized systems,",
        "In high-value transaction contexts,"
    ]

    bridges = [
        "this rarely behaves as expected without careful auditing.",
        "issues often cascade across interconnected smart contracts.",
        "failures often surface only under high transaction load or complex interactions.",
        "small coding mistakes can result in significant financial loss.",
        "what seems secure in theory can fail under real-world conditions."
    ]

    closers = [
        "which is why thorough testing and formal verification are essential.",
        "and this insight usually emerges from repeated deployment and auditing experience.",
        "making it a recurring topic in blockchain development studies.",
        "and there is rarely a single universally correct implementation.",
        "a lesson reinforced by past DeFi and NFT exploits."
    ]

    middle_sentences = [
        "Smart contract bugs can lead to exploits and irreversible financial loss.",
        "Consensus mechanism failures can compromise network integrity and transaction finality.",
        "DeFi protocol misconfigurations may result in liquidity risks and user losses.",
        "NFT marketplaces can suffer from front-running or transaction ordering issues.",
        "High gas fees can make layer 2 solutions necessary for cost-effective operations.",
        "Wallet security lapses may expose private keys to theft or phishing attacks."
    ]