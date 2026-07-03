from rag_engine.vector_store import VectorStore
from rag_engine.config import TOP_K


class Retriever:

    def __init__(self):

        vector_store = VectorStore()

        self.retriever = vector_store.as_retriever()

    def retrieve(self, question):

        return self.retriever.invoke(question)