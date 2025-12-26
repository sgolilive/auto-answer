from ingestion.content.generators.BaseGenerator import BaseGenerator

class LegalStudies(BaseGenerator):

    def get_topic(self) -> str:
        return "legal studies and ip"

    def get_subtopics(self) -> list[str]:
        return [
            "contract law", "intellectual property rights", "patent law", "trademark law",
            "copyright issues", "cyber law", "corporate law", "criminal law",
            "constitutional law", "international law",
            "contract law", "intellectual property", "corporate law", "constitutional law",
            "international law", "compliance frameworks", "dispute resolution", "labor law",
            "taxation law", "cyber law"
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
        "legal interpretation challenge", "IP enforcement problem", "contractual dispute scenario",
        "regulatory compliance issue", "litigation strategy problem", "patent infringement assessment",
        "trademark violation detection", "cybersecurity legal dilemma", "constitutional analysis difficulty", "international treaty application",
        "compliance enforcement challenge", "contract interpretation issue", "intellectual property dispute",
        "regulatory risk scenario", "cross-border legal conflict", "labor dispute resolution",
        "tax compliance problem", "cybersecurity legal liability", "constitutional interpretation challenge", "corporate governance dilemma"
    ]

    openers = [
        "In practical legal analysis,",
        "From an intellectual property perspective,",
        "During contract drafting and dispute resolution,",
        "Historically,",
        "When interpreting legal statutes and regulations,",
        "In corporate and international law contexts,",
        "In practical legal practice,",
        "From a regulatory compliance perspective,",
        "During contract negotiation and enforcement,",
        "Historically,",
        "When dealing with intellectual property issues,",
        "In corporate governance contexts,"
    ]

    bridges = [
        "this rarely behaves as expected without careful interpretation and precedent analysis.",
        "issues often propagate through multiple jurisdictions and legal frameworks.",
        "problems often surface only under nuanced or ambiguous legal language.",
        "small variations in clauses or regulations can drastically affect outcomes.",
        "what seems straightforward legally can yield unexpected judicial results.",
        "this rarely behaves as expected without careful review and due diligence.",
        "issues often propagate across multiple legal domains and jurisdictions.",
        "problems often surface only under complex or ambiguous cases.",
        "small oversights can lead to significant legal liabilities or disputes.",
        "what seems straightforward legally can have unexpected consequences in practice."
    ]

    closers = [
        "which is why meticulous legal research, compliance checks, and risk assessment are essential.",
        "and this insight usually emerges from case studies and precedent evaluation.",
        "making it a recurring topic in legal education and professional practice.",
        "and there is rarely a single universally applicable legal strategy.",
        "a lesson reinforced by real-world litigation and regulatory enforcement experiences.",
        "which is why rigorous analysis, documentation, and adherence to regulations are essential.",
        "and this insight usually emerges from real-world case studies and legal precedents.",
        "making it a recurring topic in legal education and practice.",
        "and there is rarely a single universally correct legal interpretation.",
        "a lesson reinforced by actual courtroom and compliance outcomes."
    ]

    middle_sentences = [
        "Contract law disputes often hinge on precise wording and obligations interpretation.",
        "Intellectual property cases require careful assessment of ownership, originality, and infringement.",
        "Patent and trademark enforcement can be complicated by jurisdictional and procedural differences.",
        "Cyber law challenges involve evolving technology, privacy, and cybersecurity regulations.",
        "Corporate law issues include compliance, fiduciary duties, and governance.",
        "Criminal law cases depend on evidence, precedent, and procedural correctness.",
        "Contract clauses can be interpreted differently under various jurisdictions.",
        "Intellectual property disputes require careful examination of prior art and rights.",
        "Corporate governance involves balancing stakeholder interests and compliance obligations.",
        "Labor law disputes often involve intricate rights, obligations, and precedent considerations.",
        "Taxation law requires understanding of local and international regulations to avoid penalties.",
        "Cyber law compliance is crucial for data protection, privacy, and liability mitigation."
      ]
