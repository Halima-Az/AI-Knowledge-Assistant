from rag_engine.models.rag_response import RAGResponse

class RAGPipeline:
    def __init__(self,loader,parser,splitter,vectore_store,retriever,prompt,llm,context_builder,source_builder):
        self.loader=loader 
        self.pdfParser=parser
        self.splitter=splitter
        self.vectore_store=vectore_store
        self.retriever=retriever
        self.prompt=prompt
        self.llm=llm
        self.context_builder=context_builder
        self.source_builder=source_builder
           
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
        
        sources = self.source_builder.build(documents)
        
        return RAGResponse(
            answer=response.content,
            sources=sources
        )   
            
        