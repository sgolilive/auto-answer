from ingestion.content.generators.BaseGenerator import BaseGenerator

class CyberSecurity(BaseGenerator):

    def get_topic(self) -> str:
        return "CyberSecurity"

    def get_subtopics(self) -> list[str]:
        return [
            "encryption", "firewalls", "penetration testing", "malware analysis",
            "zero trust", "SIEM", "phishing attacks", "incident response",
            "vulnerability assessment", "network security"
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
        "real-world attack scenario", "vulnerability exploitation", "risk assessment challenge",
        "security incident response", "data protection dilemma", "network breach analysis",
        "policy implementation edge case", "security monitoring failure", "threat detection scenario",
        "compliance and regulation challenge"
    ]

    openers = [
        "In real-world cybersecurity scenarios,",
        "From a threat analysis perspective,",
        "During penetration testing exercises,",
        "Historically,",
        "When managing security operations,",
        "In enterprise networks,"
    ]

    bridges = [
        "this rarely behaves as expected without careful planning.",
        "the effects often cascade across multiple systems.",
        "incidents often surface only after attackers exploit hidden vulnerabilities.",
        "misconfigurations can amplify risks significantly.",
        "what seems secure on paper can fail in practice."
    ]

    closers = [
        "which is why continuous monitoring and regular audits are critical.",
        "and this insight usually emerges from repeated incident analysis.",
        "making it a recurring topic in cybersecurity operations.",
        "and there is rarely a single universally correct defense.",
        "a lesson reinforced by real-world breach investigations."
    ]

    middle_sentences = [
        "Misconfigured firewalls or weak encryption can allow attackers to bypass defenses.",
        "Phishing attacks often exploit human vulnerabilities rather than technical flaws.",
        "Incident response plans must account for unknown or zero-day threats.",
        "Security monitoring tools may generate false positives, complicating detection.",
        "Vulnerability assessments uncover hidden dependencies that could be exploited.",
        "Zero trust implementation requires continuous verification of all access requests."
    ]