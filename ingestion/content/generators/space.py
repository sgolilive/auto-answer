from ingestion.content.generators.BaseGenerator import BaseGenerator

class SpaceTechnology(BaseGenerator):

    def get_topic(self) -> str:
        return "space technology"

    def get_subtopics(self) -> list[str]:
        return [
            "satellite systems", "rocket propulsion", "spacecraft navigation", "space mission planning",
            "orbital mechanics", "space robotics", "space communication", "remote sensing",
            "deep space exploration", "space environment effects"
        ]

    def get_sentence_pool(self) -> list[str]:
        pass

    def get_intro_options(self, subtopic: str) -> list[str]:
        pass

    def generate_question(self, subtopic: str) -> str:
        return super().generate_question(subtopic)

    def generate_answer(self, subtopic: str) -> str:
        return super().generate_answer(subtopic)

    middle_sentences = [
        "Rocket propulsion efficiency is critical for orbit insertion and fuel optimization.",
        "Satellite navigation must compensate for gravitational perturbations and orbital drift.",
        "Communication delays can affect real-time decision-making in deep space missions.",
        "Robotic operations require precise calibration and fault-tolerant control algorithms.",
        "Remote sensing instruments need careful calibration to provide accurate scientific data.",
        "Radiation exposure in space can damage both electronics and human crews."
      ]

    question_intents = [
        "orbit insertion challenge", "propulsion efficiency issue", "navigation accuracy problem",
        "mission timeline optimization", "spacecraft reliability scenario", "communication delay problem",
        "robotic arm operation", "sensor calibration challenge", "deep space anomaly", "radiation exposure risk"
    ]
    openers = [
        "In practical space missions,",
        "From a spacecraft engineering perspective,",
        "During orbital deployment experiments,",
        "Historically,",
        "When planning deep space missions,",
        "In satellite communication contexts,"
    ]

    bridges = [
        "this rarely behaves as expected without precise calculations.",
        "issues often cascade through propulsion, navigation, and communication subsystems.",
        "problems often surface only under extreme environmental conditions.",
        "small misalignments can lead to mission-critical failures.",
        "what seems feasible in simulation can fail in actual space operations."
    ]

    closers = [
        "which is why rigorous testing and simulation are essential.",
        "and this insight usually emerges from repeated mission planning and analysis.",
        "making it a recurring topic in space technology studies.",
        "and there is rarely a single universally correct engineering solution.",
        "a lesson reinforced by real-world spacecraft operations and mission reports."
    ]
