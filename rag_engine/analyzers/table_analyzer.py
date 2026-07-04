from langchain_core.documents import Document

from rag_engine.models.extracted_table import ExtractedTable


class TableAnalyzer:

    def analyze(self, extracted_table: ExtractedTable) -> Document:

        table_text = extracted_table.dataframe.to_markdown(index=False)

        return Document(
            page_content=table_text,
            metadata={
                "page": extracted_table.page,
                "content_type": "table"
            }
        )