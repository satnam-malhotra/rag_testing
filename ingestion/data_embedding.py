import pymupdf
from sentence_transformers import SentenceTransformer


class DataEmbedding:

    def __init__(self, file_path, chunk_size):
        self.chunk_size = chunk_size
        self.file_path = file_path
        self.chunks = []
        self.embedding_modal = None
        self.embeddings = None

    def data_chunks(self):
        text = ""
        doc = pymupdf.open(self.file_path)
        for page in doc:
            text += page.get_text()
        for index in range(0, len(text), self.chunk_size):
            self.chunks.append(text[index:index + self.chunk_size])

    def load_embedding_modal(self):
        self.embedding_modal = SentenceTransformer(
            "all-MiniLM-L6-v2"
        )

    def embedd_chunks(self):
        self.data_chunks()
        self.load_embedding_modal()
        self.embeddings = self.embedding_modal.encode(
            self.chunks,
        ).tolist()


    # def initialize_vector_db(self):
    #     db = chromadb.PersistentClient(path = "./vector_db")
    #     collection = db.get_or_create_collection(name = "pdf_knowledge_Base")

    # def store_embeddings_in_chromadb(self, chunks, embeddings):
    #     collection.add(embeddings = embeddings, documents = chunks, ids=[str(index) for index in range(len(chunks))])
    #     print("Embeddings stored in Vector DB")