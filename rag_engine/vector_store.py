from langchain_chroma import Chroma

from rag_engine.embeddings.embeddig_service import EmbeddingProvider
from rag_engine.config import (
    CHROMA_COLLECTION_NAME,
    CHROMA_DB_DIRECTORY,
    TOP_K
)

 
class VectorStore:

    def __init__(self):

        embeddings = EmbeddingProvider().get_embeddings()

        self.db = Chroma(

            collection_name=CHROMA_COLLECTION_NAME,

            embedding_function=embeddings,

            persist_directory=CHROMA_DB_DIRECTORY
        )
        
    def add_documents(self,docs):
        self.db.add_documents(docs) 
        
    def as_retriever(self):
        return self.db.as_retriever(
            search_kwargs={"k":TOP_K}
        )      