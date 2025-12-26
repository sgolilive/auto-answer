from ingestion.content.generators.BaseGenerator import BaseGenerator

class Networking(BaseGenerator):

    def get_topic(self) -> str:
        return "Networking and Protocols"

    def get_subtopics(self) -> list[str]:
        return [
            "TCP/IP", "DNS", "routing", "VPN", "QoS", "NAT",
            "HTTP/HTTPS", "network security", "firewalls", "load balancing"
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
        "network performance analysis", "protocol failure scenario", "routing conflict challenge",
        "security breach evaluation", "packet loss investigation", "latency troubleshooting",
        "VPN deployment edge case", "QoS configuration challenge", "DNS resolution failure", "firewall misconfiguration impact"
    ]

    openers = [
        "In real-world networking scenarios,",
        "From a protocol analysis perspective,",
        "During network troubleshooting exercises,",
        "Historically,",
        "When configuring enterprise networks,",
        "In performance-critical systems,"
    ]

    bridges = [
        "this rarely behaves as expected without careful configuration.",
        "effects often propagate through interconnected devices.",
        "issues often surface only under high load or unusual traffic patterns.",
        "misconfigurations can amplify latency or packet loss.",
        "what seems straightforward can fail under real network conditions."
    ]

    closers = [
        "which is why monitoring and simulation are critical for robust networks.",
        "and this insight usually emerges from repeated testing and analysis.",
        "making it a recurring topic in network engineering studies.",
        "and there is rarely a single universally correct setup.",
        "a lesson reinforced by troubleshooting real-world network incidents."
    ]

    middle_sentences = [
        "TCP/IP misconfigurations can lead to connectivity failures or unexpected routing loops.",
        "DNS resolution issues can disrupt services and affect dependent applications.",
        "VPN setups sometimes fail due to encryption negotiation problems or policy conflicts.",
        "QoS misconfigurations can lead to traffic prioritization issues affecting performance.",
        "Firewall rules can block legitimate traffic or allow unintended access.",
        "Load balancing misalignment may result in uneven traffic distribution and server overloads."
      ]
