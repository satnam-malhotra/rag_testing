import chromadb

class StoreEmbeddings:

    def __init__(self):
        self.collection = None

    def initialize_vector_db(self):
        db = chromadb.PersistentClient(path ="../vector_db")
        self.collection = db.get_or_create_collection(name = "pdf_knowledge_Base")
        print("initialized vector db")

    def store_embeddings_in_chromadb(self, embeddings, chunks):
        self.initialize_vector_db()
        self.collection.add(embeddings = embeddings,
                            documents = chunks,
                            ids=[str(index) for index in range(len(chunks))])
        print("Embeddings stored in Vector DB")
