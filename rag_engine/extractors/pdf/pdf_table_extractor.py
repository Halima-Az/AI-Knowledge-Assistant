
import fitz

from ..base_extractor import BaseExtractor
from ...models.extracted_table import ExtractedTable

class PDFTableExtractor(BaseExtractor):
    
    def extract(self, pdf:fitz.Document)-> list[ExtractedTable]:
        
        extracted_tables = []

        for page_number, page in enumerate(pdf, start=1):

            tables = page.find_tables()

            for table in tables.tables:

                dataframe = table.to_pandas()

                extracted_tables.append(
                    ExtractedTable(
                        dataframe=dataframe,
                        page=page_number
                    )
                )

        return extracted_tables
        
        