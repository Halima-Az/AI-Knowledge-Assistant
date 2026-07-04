import fitz
from .base_loader import BaseLoader

class PDFLoader(BaseLoader):
    
    def load(self, source:str)->fitz.Document:
        
        return fitz.open(source)