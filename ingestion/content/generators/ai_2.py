from ingestion.content.generators.BaseGenerator import BaseGenerator

class AIRobotics(BaseGenerator):

    def get_topic(self) -> str:
        return "AI and Robotics"

    def get_subtopics(self) -> list[str]:
        return [
            "machine learning algorithms", "reinforcement learning", "robot perception",
            "computer vision", "natural language processing", "robot motion planning",
            "multi-agent systems", "human-robot interaction", "autonomous systems", "AI ethics and safety"
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
            "algorithmic performance challenge", "policy optimization problem", "perception error scenario",
            "image recognition difficulty", "language understanding problem", "trajectory planning issue",
            "collaboration complexity", "interaction safety concern", "autonomy validation challenge", "ethical dilemma"
        ]

    openers = [
            "In practical AI experiments,",
            "From a robotics perspective,",
            "During machine learning model evaluation,",
            "Historically,",
            "When analyzing perception and decision-making systems,",
            "In autonomous system design contexts,"
        ]

    bridges = [
            "this rarely behaves as expected without careful training, testing, and validation.",
            "issues often propagate through data preprocessing, model selection, and deployment steps.",
            "problems often surface only under edge cases or real-world operational conditions.",
            "small variations in input or environment can drastically affect system performance.",
            "what seems theoretically optimal can fail when applied in dynamic, unstructured environments."
        ]

    closers = [
        "which is why rigorous experimentation, simulation, and iterative design are essential.",
        "and this insight usually emerges from repeated trials and performance benchmarking.",
        "making it a recurring topic in AI and robotics education and research.",
        "and there is rarely a single universally optimal solution for complex AI-robotic tasks.",
        "a lesson reinforced by real-world deployments and human-robot collaboration studies."
    ]

    middle_sentences = [
                "Machine learning algorithms may fail under distribution shifts or biased datasets.",
                "Reinforcement learning requires careful reward shaping and exploration strategies.",
                "Robot perception can be affected by sensor noise, occlusion, and environmental variability.",
                "Computer vision models often need large annotated datasets and robust preprocessing.",
                "Natural language processing systems face challenges with context, ambiguity, and rare phrases.",
                "Autonomous motion planning demands real-time optimization and collision avoidance."
            ]