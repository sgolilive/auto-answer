from ingestion.content.generators.BaseGenerator import BaseGenerator

class EdgeComputing(BaseGenerator):

    def get_topic(self) -> str:
        return "ai and edge computing"

    def get_subtopics(self) -> list[str]:
        return [
            "sensor networks", "edge device management", "real-time data processing", "IoT security",
            "low-power communication protocols", "data aggregation and filtering", "fog computing",
            "device interoperability", "cloud-edge integration", "predictive maintenance"
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
        "latency reduction challenge", "data reliability issue", "device authentication problem",
        "real-time processing bottleneck", "protocol scalability problem", "edge storage limitation",
        "interoperability conflict", "security vulnerability scenario", "energy efficiency optimization", "predictive analytics accuracy"
    ]

    openers = [
        "In practical IoT deployments,",
        "From an edge computing perspective,",
        "During sensor network experiments,",
        "Historically,",
        "When designing low-latency IoT systems,",
        "In device interoperability contexts,"
    ]

    bridges = [
        "this rarely behaves as expected without careful network and protocol management.",
        "issues often propagate through edge processing, communication, and storage subsystems.",
        "problems often surface only under high device density or variable connectivity conditions.",
        "small synchronization errors can drastically affect real-time analytics and automation.",
        "what seems optimal in lab simulations can fail under large-scale deployment."
    ]

    closers = [
        "which is why iterative testing and monitoring strategies are essential.",
        "and this insight usually emerges from repeated field trials and network analysis.",
        "making it a recurring topic in IoT and edge computing studies.",
        "and there is rarely a single universally correct solution for heterogeneous devices.",
        "a lesson reinforced by real-world IoT network and edge system deployments."
    ]

    middle_sentences = [
        "Sensor networks must handle variable connectivity and interference while maintaining data reliability.",
        "Edge devices require optimized resource management to perform real-time analytics efficiently.",
        "Security and authentication challenges are critical to prevent unauthorized access and data breaches.",
        "Data aggregation and filtering strategies are essential for reducing latency and bandwidth usage.",
        "Low-power communication protocols must balance energy efficiency with transmission reliability.",
        "Cloud-edge integration requires careful design to maintain consistency and availability of data."
      ]
