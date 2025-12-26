from ingestion.content.generators.BaseGenerator import BaseGenerator

class QuantumComputing(BaseGenerator):

    def get_topic(self) -> str:
        return "quantum computing"

    def get_subtopics(self) -> list[str]:
        return [
            "qubits and superposition", "entanglement", "quantum gates", "quantum circuits",
            "quantum algorithms", "error correction", "quantum decoherence", "measurement in quantum systems",
            "quantum supremacy", "quantum cryptography",
            "quantum error correction", "quantum communication", "quantum complexity theory",
            "quantum teleportation", "information encoding and decoding"
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
        "Superposition introduces challenges in measuring and collapsing qubit states accurately.",
        "Entanglement requires precise synchronization and isolation to maintain coherence.",
        "Quantum gates are prone to noise and fidelity issues impacting computation results.",
        "Error correction protocols are essential to mitigate decoherence and qubit loss.",
        "Scaling qubits while maintaining fidelity remains a central engineering challenge.",
        "Quantum cryptography relies on fundamental principles that can be disrupted by environmental factors."
      ]

    question_intents = [
        "quantum algorithm efficiency challenge", "error correction scenario",
        "decoherence problem analysis", "entanglement utilization issue", "quantum measurement uncertainty",
        "quantum gate fidelity assessment", "circuit optimization challenge", "cryptography application scenario",
        "qubit scaling limitation", "quantum supremacy claim evaluation"
    ]

    openers = [
        "In practical quantum computing scenarios,",
        "From a quantum algorithm perspective,",
        "During qubit system experiments,",
        "Historically,",
        "When implementing quantum circuits,",
        "In high-complexity quantum applications,"
    ]

    bridges = [
        "this rarely behaves as expected without careful calibration.",
        "issues often propagate through entangled qubits and gates.",
        "problems often surface only under multiple superposition interactions.",
        "small errors can quickly accumulate, affecting computation fidelity.",
        "what seems theoretically sound can fail in experimental setups."
    ]

    closers = [
        "which is why error correction and careful testing are critical.",
        "and this insight usually emerges from repeated experimentation and simulations.",
        "making it a recurring topic in quantum computing research.",
        "and there is rarely a single universally correct implementation.",
        "a lesson reinforced by real-world quantum experiments and benchmarks."
    ]
