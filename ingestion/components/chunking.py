from typing import Any, Iterator, Dict, List

from nltk.tokenize import sent_tokenize
from ingestion.entities.embedder import Embedder
from logger import get_logger

class Chunking:

    MAX_QA_TOKENS = 800

    def __init__(self, embedder: Embedder):
        self.embedder = embedder
        self.logger = get_logger(__name__)

    def _truncate_to_tokens(self, qa: Dict[str, Any]) -> str:
        qa_text = (
            f'Question: {qa["question"]}\n'
            f'Answer: {qa["answer"]}'
        )

        tokens = qa_text.split()

        if len(tokens) > self.MAX_QA_TOKENS:
            tokens = tokens[:self.MAX_QA_TOKENS]

        return ' '.join(tokens)

    def chunk_answer_text(self, qas: Iterator[Dict[str, Any]]) -> Iterator[Dict[str, Any]]:

        for qa in qas:
            current_chunks = self._sentence_aware_chunks(qa['answer'])

            # Compute once per QA
            qa_embedding = self.embedder.embed(self._truncate_to_tokens(qa))

            total_chunks = len(current_chunks)

            for i, chunk in enumerate(current_chunks):
                yield {
                    'chunk_text': chunk,
                    'embeddings': self.embedder.embed(chunk),
                    'qa_embeddings': qa_embedding,
                    'q_text': qa["question"],
                    'metadata': {
                        'qid': qa['qid'],
                        'chunk_index': i,
                        'total_chunks': total_chunks,
                        'topic': qa['topic'],
                        'subtopic': qa['subtopic'],
                    }
                }

    def _sentence_aware_chunks(self, answer_text: str, chunk_size: int = 500) -> List[str]:

        sentences = sent_tokenize(answer_text)
        chunks: List[str] = []
        current_chunk: List[str] = []
        current_len = 0

        for s in sentences:
            token_len = len(s.split())

            if current_len + token_len > chunk_size and current_chunk:
                chunks.append(" ".join(current_chunk))
                current_chunk = []
                current_len = 0

            current_chunk.append(s)
            current_len += token_len

        if current_chunk:
            chunks.append(" ".join(current_chunk))

        return chunks