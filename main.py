
from rag_engine.pipeline import RAGPipeline
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

    pipeline = RAGPipeline()

    pdf_path = "documents/testpdf.pdf"

    print("Indexation en cours...")

    pipeline.index_documents(pdf_path)

    print("Indexation terminée.\n")

    while True:

        question = input("Votre question : ")

        if question.lower() == "exit":
            break

        answer = pipeline.ask(question)

        print("\nRéponse :")
        print(answer)
        print()


if __name__ == "__main__":
    main()