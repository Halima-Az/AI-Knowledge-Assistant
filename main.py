
from rag_engine.pipeline import RAGPipeline
from rag_engine.container.service_container import ServiceContainer
"""
from rag_engine.loaders.pdf_loader import PDFLoader

from rag_engine.splitters.text_spliter import TextSplitterService

loader = PDFLoader()

documents = loader.load("documents/RAG_Guide_Complet.pdf")

splitter = TextSplitterService()

chunks = splitter.split(documents)

print(f"Nombre de chunks : {len(chunks)}")

"""
def main():

    container=ServiceContainer()
    pipeline= container.create_pipeline()
    
    pdf_path = "documents/testpdf.pdf"

    print("Indexation en cours...")

    pipeline.index_documents(pdf_path)

    print("Indexation terminée.\n")

    while True:

        question = input("Votre question : ")

        if question.lower() == "exit":
            break

        response = pipeline.ask(question)

        print("\nRéponse :")
        print(response.answer)
        print("\n Sources : \n")
        for source in response.sources:
            print(f"- page {source.page} |"
                f"Source : {source.content_type}")


if __name__ == "__main__":
    main()