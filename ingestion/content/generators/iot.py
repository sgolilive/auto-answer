from ingestion.content.generators.BaseGenerator import BaseGenerator

class IoT(BaseGenerator):

    def get_topic(self) -> str:
        return "IoT"

    def get_subtopics(self) -> list[str]:
        return [
            "sensor networks", "actuator control", "edge computing", "IoT protocols (MQTT, CoAP)",
            "device authentication", "data aggregation", "low-power design", "real-time monitoring",
            "IoT security", "cloud integration"
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
        "network congestion scenario", "device authentication failure", "edge processing challenge",
        "real-time data collection problem", "low-power optimization issue", "protocol compatibility challenge",
        "IoT security breach", "data aggregation inconsistency", "cloud integration delay", "actuator control failure"
    ]

    openers = [
        "In practical IoT deployment scenarios,",
        "From an edge computing perspective,",
        "During sensor network experiments,",
        "Historically,",
        "When designing low-power IoT systems,",
        "In device-cloud integration contexts,"
    ]

    bridges = [
        "this rarely behaves as expected without careful configuration.",
        "issues often cascade through multiple devices and protocols.",
        "problems often surface only under large-scale deployments.",
        "small misconfigurations can compromise both performance and security.",
        "what seems functional in testing can fail in real-world network conditions."
    ]

    closers = [
        "which is why continuous monitoring and proper protocol management are essential.",
        "and this insight usually emerges from repeated deployment and testing cycles.",
        "making it a recurring topic in IoT system engineering.",
        "and there is rarely a single universally correct implementation.",
        "a lesson reinforced by real-world IoT failures and successes."
    ]

    middle_sentences = [
        "Sensor networks may experience latency or data loss under high traffic conditions.",
        "Actuator control failures can disrupt automation tasks if communication is unreliable.",
        "Edge computing nodes need optimized resource allocation to maintain responsiveness.",
        "IoT security breaches can occur if devices are improperly authenticated or patched.",
        "Low-power designs must balance energy efficiency with data reliability.",
        "Cloud integration challenges may delay real-time monitoring or analytics."
      ]