from sentence_transformers import SentenceTransformer

class Embedder:

  def __init__(self, model_name="all-MiniLM-L6-v2"): #384 embeddings
    self.model = SentenceTransformer(model_name)

  def embed(self, text: str):
    return self.model.encode(text,
            convert_to_numpy=True,
            normalize_embeddings=True,
            show_progress_bar=False)