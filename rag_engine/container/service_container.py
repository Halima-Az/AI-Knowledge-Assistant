from rag_engine.loaders.pdf_loader import PDFLoader
from rag_engine.parsers.pdf_parser import PDFParser
from rag_engine.splitters.text_spliter import TextSplitterService
from rag_engine.vector_store import VectorStore
from rag_engine.retriever import Retriever
from rag_engine.prompt_builder import PromptBuilder
from rag_engine.builders.context_builder import ContextBuilder
from rag_engine.builders.source_builder import SourceBuilder
from rag_engine.llm import LLMProvider
from rag_engine.pipeline import RAGPipeline


class ServiceContainer:

    def create_pipeline(self):

        loader = PDFLoader()

        parser = PDFParser()

        splitter = TextSplitterService()

        vector_store = VectorStore()

        retriever = Retriever()

        prompt = PromptBuilder().get_prompt()

        llm = LLMProvider().get_llm()

        context_builder = ContextBuilder()

        source_builder = SourceBuilder()

        return RAGPipeline(
            loader=loader,
            parser=parser,
            splitter=splitter,
            vector_store=vector_store,
            retriever=retriever,
            prompt=prompt,
            llm=llm,
            context_builder=context_builder,
            source_builder=source_builder,
        )