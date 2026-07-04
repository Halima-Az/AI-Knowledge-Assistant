from docx import Document

from .base_loader import BaseLoader


class WordLoader(BaseLoader):

    def load(self, source: str) -> Document:

        return Document(source)