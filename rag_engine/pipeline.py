from rag_engine.ingestion.pdf_loader import PDFLoader
from rag_engine.splitters.text_spliter import TextSplitterService
from  rag_engine.vector_store import VectorStore
from rag_engine.retriever import Retriever
from rag_engine.prompt_builder import PromptBuilder
from rag_engine.llm import LLMProvider
from rag_engine.parsers.pdf_parser import PDFParser
from rag_engine.models.rag_response import RAGResponse
from rag_engine.builders.context_builder import ContextBuilder 
from rag_engine.models.source_reference import SourceReference
class RAGPipeline:
    def __init__(self):
        self.loader=PDFLoader()
        self.splitter=TextSplitterService()
        self.vectore_store=VectorStore()
        self.retriever=Retriever()
        self.prompt=PromptBuilder().get_prompt()
        self.llm=LLMProvider().get_llm()
        self.pdfParser=PDFParser()
        self.context_builder=ContextBuilder()
           
    # Indexation : docs -> splitter -> chunks -> embedding -> store in chromaDB   
    def index_documents(self,doc_path):
        pdf=self.loader.load(doc_path)
        documents=self.pdfParser.parse(pdf)
        chunks=self.splitter.split(documents)
        self.vectore_store.add_documents(chunks)
        
    # Q/R : question -> retriver -> TOP K docs -> prompt -> LLM -> Response
    def ask(self, question):

        documents = self.retriever.retrieve(question)

        context = self.context_builder.build(documents)

        messages = self.prompt.invoke(
            {
                "context": context,
                "question": question
            }
        )

        response = self.llm.invoke(messages)
        
        sources = []
        seen = set()

        for doc in documents:

            ref = SourceReference(
                source=doc.metadata.get("source", "Unknown"),
                page=doc.metadata.get("page", -1),
                content_type=doc.metadata.get("content_type", "text"),
            )

            key = (ref.source, ref.page, ref.content_type)

            if key not in seen:
                seen.add(key)
                sources.append(ref)

        return RAGResponse(
            answer=response.content,
            sources=sources
        )   
            
        