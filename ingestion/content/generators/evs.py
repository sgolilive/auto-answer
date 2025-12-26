from ingestion.content.generators.BaseGenerator import BaseGenerator

class EnvironmentalScience(BaseGenerator):

    def get_topic(self) -> str:
        return "environmental science and sustainability"

    def get_subtopics(self) -> list[str]:
        return [
            "climate change", "biodiversity conservation", "renewable energy",
            "waste management", "ecosystem services", "water resources",
            "air pollution control", "sustainable agriculture", "environmental policy", "carbon footprint analysis"
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
        "emission reduction challenge", "conservation strategy problem", "renewable adoption scenario",
        "pollution mitigation issue", "resource management difficulty", "policy implementation problem",
        "sustainability assessment challenge", "ecosystem impact evaluation", "climate adaptation problem", "carbon accounting complexity"
    ]

    openers = [
        "In practical environmental studies,",
        "From a sustainability perspective,",
        "During ecosystem management exercises,",
        "Historically,",
        "When analyzing renewable energy systems,",
        "In environmental policy and regulation contexts,"
    ]

    bridges = [
        "this rarely behaves as expected without comprehensive system analysis and stakeholder engagement.",
        "issues often propagate through multiple ecological, economic, and social layers.",
        "problems often surface only under extreme environmental stressors or policy constraints.",
        "small variations in implementation can drastically affect ecological and economic outcomes.",
        "what seems theoretically sustainable can fail under real-world operational conditions."
    ]

    closers = [
        "which is why careful planning, monitoring, and adaptive management are essential.",
        "and this insight usually emerges from longitudinal studies and impact assessments.",
        "making it a recurring topic in environmental science and sustainability education.",
        "and there is rarely a single universally correct strategy for complex environmental problems.",
        "a lesson reinforced by real-world conservation, policy, and sustainability initiatives."
    ]

    middle_sentences = [
        "Climate change mitigation requires coordinated action across multiple sectors and regions.",
        "Biodiversity conservation strategies must consider habitat connectivity and species interactions.",
        "Renewable energy adoption is influenced by technology, policy, and market incentives.",
        "Waste management challenges include resource recovery, pollution control, and behavioral change.",
        "Water resource management demands balancing human needs with ecological sustainability.",
        "Environmental policies often require monitoring, enforcement, and adaptive updates."
      ]