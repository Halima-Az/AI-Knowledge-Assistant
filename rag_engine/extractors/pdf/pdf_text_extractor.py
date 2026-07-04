import fitz

from langchain_core.documents import Document

from rag_engine.extractors.base_extractor import BaseExtractor


class PDFTextExtractor(BaseExtractor):
    """
    Extrait le texte d'un document PDF
    et le convertit en objets Document LangChain.
    """

    def extract(self, pdf: fitz.Document) -> list[Document]:

        documents = []

        source = pdf.name

        for page_number, page in enumerate(pdf, start=1):

            text = page.get_text("text").strip()

            if not text:
                continue

            documents.append(
                Document(
                    page_content=text,
                    metadata={
                        "source": source,
                        "page": page_number,
                        "content_type": "text"
                    }
                )
            )

        return documents