from langchain_text_splitters import RecursiveCharacterTextSplitter

from rag_engine.config import (
    CHUNK_SIZE,
    CHUNK_OVERLAP,
    SEPARATORS
)

class TextSplitterService:

    def __init__(self):

        self.splitter = RecursiveCharacterTextSplitter(

            chunk_size=CHUNK_SIZE,

            chunk_overlap=CHUNK_OVERLAP,

            separators=SEPARATORS
        )

    def split(self, documents):

        return self.splitter.split_documents(documents)