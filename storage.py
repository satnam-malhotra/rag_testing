import chromadb

class StoreEmbeddings:

    def __init__(self):
        self.collection = None

    def initialize_vector_db(self):
        db = chromadb.PersistentClient(path = "./vector_db")
        self.collection = db.get_or_create_collection(name = "pdf_knowledge_Base")
        print("initialized vector db")

    def store_embeddings_in_chromadb(self, embeddings, chunks):
        self.initialize_vector_db()
        self.collection.add(embeddings = embeddings,
                            documents = chunks,
                            ids=[str(index) for index in range(len(chunks))])
        print("Embeddings stored in Vector DB")



# # Initialize chromadb and create collection from the given file
# def initialize_chromadb():
#     chroma_client = chromadb.PersistentClient(path="./chroma_db")
#     print("Chromadb initialized")
#     return chroma_client.get_or_create_collection(name="pdf_knowledge")
#
#
# def generate_and_store_embedding():
#     chunks = read_chunks()
#     embedding = get_embedding(chunks)
#     collection = initialize_chromadb()
#     collection.add(documents=chunks, embeddings=embedding, ids=[str(index) for index in range(len(chunks))])
#     print("Embedding stored successfully. Ingestion completed")