
CHUNK_SIZE = 800

CHUNK_OVERLAP = 150

SEPARATORS = [
    "\n\n",
    "\n",
    " ",
    ""
]

# Embeddings
EMBEDDING_MODEL = "sentence-transformers/all-MiniLM-L6-v2"

# ChromaDB
CHROMA_COLLECTION_NAME = "knowledge_base"

CHROMA_DB_DIRECTORY = "./chroma_db"

# Retriver 
TOP_K=5

# tesseract path
TESSERACT_PATH = r"C:\Program Files\Tesseract-OCR\tesseract.exe"