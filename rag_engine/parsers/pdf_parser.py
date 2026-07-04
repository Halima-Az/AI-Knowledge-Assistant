import fitz

from rag_engine.parsers.base_parser import BaseParser

from rag_engine.extractors.pdf.pdf_text_extractor import PDFTextExtractor
from rag_engine.extractors.pdf.pdf_image_extractor import PDFImageExtractor
from rag_engine.extractors.pdf.pdf_table_extractor import PDFTableExtractor

from rag_engine.analyzers.image_analyzer import ImageAnalyzer
from rag_engine.analyzers.table_analyzer import TableAnalyzer


class PDFParser(BaseParser):

    def __init__(self):

        self.text_extractor = PDFTextExtractor()

        self.image_extractor = PDFImageExtractor()

        self.table_extractor = PDFTableExtractor()

        self.image_analyzer = ImageAnalyzer()

        self.table_analyzer = TableAnalyzer()

    def parse(self, pdf: fitz.Document):

        documents = []

        # Texte
        documents.extend(
            self.text_extractor.extract(pdf)
        )

        # Images
        extracted_images = self.image_extractor.extract(pdf)
        print(f"Images détectées : {len(extracted_images)}")

        for image in extracted_images:
            doc = self.image_analyzer.analyze(image)
            documents.append(doc)

        # Tableaux
        extracted_tables = self.table_extractor.extract(pdf)

        for table in extracted_tables:

            documents.append(
                self.table_analyzer.analyze(table)
            )

        return documents