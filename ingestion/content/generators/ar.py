from ingestion.content.generators.BaseGenerator import BaseGenerator

class ARVR(BaseGenerator):

    def get_topic(self) -> str:
        return "AR and VR"

    def get_subtopics(self) -> list[str]:
        return [
            "head-mounted displays (HMDs)", "motion tracking", "spatial mapping", "user interaction design",
            "rendering optimization", "latency and frame rates", "augmented overlays", "VR locomotion",
            "hardware-software integration", "multi-user AR/VR experiences"
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
        "motion sickness mitigation", "tracking accuracy challenge", "spatial mapping issue",
        "rendering performance optimization", "user interface usability problem", "latency reduction scenario",
        "augmented content alignment", "multi-user synchronization problem", "hardware integration complexity",
        "cross-platform compatibility challenge"
    ]

    openers = [
        "In practical AR/VR development scenarios,",
        "From a user experience perspective,",
        "During rendering and tracking experiments,",
        "Historically,",
        "When designing immersive environments,",
        "In multi-user AR/VR contexts,"
    ]

    bridges = [
        "this rarely behaves as expected without precise calibration.",
        "issues often cascade across hardware, software, and user perception.",
        "problems often surface only under complex interactive conditions.",
        "small misalignments can disrupt immersion or cause discomfort.",
        "what seems intuitive in simulation can fail in actual user trials."
    ]

    closers = [
        "which is why iterative testing and optimization are essential.",
        "and this insight usually emerges from repeated development and user studies.",
        "making it a recurring topic in AR/VR research and practice.",
        "and there is rarely a single universally correct implementation.",
        "a lesson reinforced by real-world immersive experience deployment."
    ]

    middle_sentences = [
                "Motion tracking errors can disrupt user immersion and cause discomfort.",
                "Latency and low frame rates may induce motion sickness or reduce responsiveness.",
                "Spatial mapping inaccuracies can misalign virtual content with real-world objects.",
                "Rendering optimization is critical to maintain visual fidelity across devices.",
                "User interaction design must balance intuitiveness with physical limitations.",
                "Hardware-software integration challenges can cause unpredictable system behavior."
            ]