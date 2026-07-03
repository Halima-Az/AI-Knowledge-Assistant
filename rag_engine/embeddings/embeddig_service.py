
from langchain_huggingface import HuggingFaceEmbeddings

from rag_engine.config import EMBEDDING_MODEL


class EmbeddingProvider:

    def __init__(self):

        self.embeddings = HuggingFaceEmbeddings(
            model_name=EMBEDDING_MODEL
        )

    def get_embeddings(self):
        return self.embeddings