import chromadb

from pathlib import Path

PROJECT_ROOT = Path(__file__).resolve().parents[2]
CHROMA_DIR = PROJECT_ROOT / "chroma_store"

class VectorDB:
    def __init__(self):
        self.client = chromadb.PersistentClient(
            path=str(CHROMA_DIR)
        )
        self.collection = self.client.get_or_create_collection(
            name='qa_collection'
        )

    batch = 100
    buffer = []

    def upsert(self, records):

        for r in records:
            self.buffer.append(r)

            if len(self.buffer) >= self.batch:
                self._persist_records()

        if self.buffer and len(self.buffer) > 0:
            self._persist_records()

    def _persist_records(self):
        ids = []
        embeddings = []
        documents = []
        metadatas = []

        for r in self.buffer:
            qid = r['metadata']['qid']

            ids.append(f"{qid}:chunk:{r['metadata']['chunk_index']}")
            embeddings.append(r['embeddings'])
            documents.append(r['chunk_text'])
            metadatas.append({
                **r['metadata'],
                'embedding_type': 'chunk'
            })

            if r['metadata']['chunk_index'] == 0:
                ids.append(f'{qid}:qa')
                embeddings.append(r['qa_embeddings'])
                documents.append(r['q_text'])
                metadatas.append({
                    'qid': qid,
                    'topic': r['metadata']['topic'],
                    'subtopic': r['metadata']['subtopic'],
                    'embedding_type': 'qa'
                })

        self.collection.upsert(ids=ids, embeddings=embeddings, documents=documents, metadatas=metadatas)
        self.buffer = []


    # def _query_data(self, query_embedding, top_k=5, include=None, filters=None):
    #     return self.collection.query(
    #         query_embeddings=[query_embedding],
    #         n_results=top_k,
    #         include=include,
    #         where= filters)

    def query(self, query_embedding, top_k=5, include=None, filters=None):
        return self.collection.query(
            query_embeddings=[query_embedding],
            n_results=top_k,
            include=include,
            where=filters #{'embedding_type':'chunk'} if filters is None else { **filters, 'embedding_type':'chunk' }
        )
