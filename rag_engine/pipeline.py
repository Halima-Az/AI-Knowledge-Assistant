from rag_engine.loaders.pdf_loader import PDFLoader
from rag_engine.splitters.text_spliter import TextSplitterService
from  rag_engine.vector_store import VectorStore
from rag_engine.retriever import Retriever
from rag_engine.prompt_builder import PromptBuilder
from rag_engine.llm import LLMProvider


class RAGPipeline:
    def __init__(self):
        self.loader=PDFLoader()
        self.splitter=TextSplitterService()
        self.vectore_store=VectorStore()
        self.retriever=Retriever()
        self.prompt=PromptBuilder().get_prompt()
        self.llm=LLMProvider().get_llm()
        
    # doc to str
    def _format_context(self, docs):
        return "\n\n----------------------\n\n".join(
            doc.page_content
            for doc in docs
        )
        
     
    # Indexation : docs -> splitter -> chunks -> embedding -> store in chromaDB   
    def index_documents(self,doc_path):
        documents=self.loader.load(doc_path)
        chunks=self.splitter.split(documents)
        self.vectore_store.add_documents(chunks)
        
    # Q/R : question -> retriver -> TOP K docs -> prompt -> LLM -> Response
    def ask(self, question):

        documents = self.retriever.retrieve(question)

        context = self._format_context(documents)

        messages = self.prompt.invoke(
            {
                "context": context,
                "question": question
            }
        )

        response = self.llm.invoke(messages)

        return response.content     
            
        