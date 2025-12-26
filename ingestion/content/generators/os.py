from ingestion.content.generators.BaseGenerator import BaseGenerator

class OperatingSystems(BaseGenerator):

    def get_topic(self) -> str:
        return "Operating Systems"

    def get_subtopics(self) -> list[str]:
        return [
            "process management", "threads", "scheduling algorithms", "virtual memory",
            "file systems", "concurrency", "deadlocks", "I/O management",
            "resource allocation", "inter-process communication"
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
        "Deadlocks can halt system processes if resource allocation is not carefully managed.",
        "Thread synchronization issues may lead to race conditions and unpredictable behavior.",
        "Scheduling algorithms need to balance throughput, latency, and fairness.",
        "Virtual memory mismanagement can cause thrashing and performance degradation.",
        "File system inconsistencies can corrupt critical data if not monitored.",
        "I/O bottlenecks may arise from unoptimized access patterns or hardware limitations."
      ]

    question_intents = [
        "resource contention scenario", "deadlock handling challenge",
        "scheduling optimization problem", "memory allocation analysis",
        "file system corruption investigation", "thread synchronization issue",
        "process starvation evaluation", "I/O bottleneck troubleshooting",
        "inter-process communication failure", "system stability assessment"
    ]

    openers = [
        "In practical OS scenarios,",
        "From a system performance perspective,",
        "During process scheduling exercises,",
        "Historically,",
        "When managing operating system resources,",
        "In multitasking environments,"
    ]

    bridges = [
        "this rarely behaves as expected without careful design.",
        "effects often propagate across multiple system components.",
        "issues often surface only under heavy load or concurrent operations.",
        "small misconfigurations can lead to severe performance degradation.",
        "what seems straightforward can fail under real-world system conditions."
    ]

    closers = [
        "which is why monitoring and careful resource management are critical.",
        "and this insight usually emerges from repeated system testing and analysis.",
        "making it a recurring topic in OS research and practice.",
        "and there is rarely a single universally correct approach.",
        "a lesson reinforced by practical OS troubleshooting and experimentation."
    ]