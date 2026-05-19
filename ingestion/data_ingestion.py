import pymupdf
from sentence_transformers import SentenceTransformer


class DataIngestion:

    def __init__(self):
        self.chunks = []
        self.embedding_modal = None
        self.embeddings = None

    def data_chunks(self, file_path, chunk_size):
        text = ""
        doc = pymupdf.open(file_path)
        for page in doc:
            text += page.get_text()
        for index in range(0, len(text), chunk_size):
            self.chunks.append(text[index:index + chunk_size])

    def load_embedding_modal(self):
        self.embedding_modal = SentenceTransformer(
            "all-MiniLM-L6-v2"
        )

    def embedd_chunks(self, file_path, chunk_size):
        self.data_chunks(file_path, chunk_size)
        self.load_embedding_modal()
        self.embeddings = self.embedding_modal.encode(
            self.chunks,
        ).tolist()
