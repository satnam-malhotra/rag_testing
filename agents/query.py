import ollama

from ingestion.data_ingestion import DataIngestion
from storage.storage import StoreEmbeddings


class QuerySearch(DataIngestion, StoreEmbeddings):

    def __init__(self, user_query):
        super().__init__()
        self.query_embeddings = None
        self.retrieved_chunks = None
        self.user_query = user_query

    def query_retrieval(self):
        self.load_embedding_modal()
        self.query_embeddings = self.embedding_modal.encode(self.user_query).tolist()

    def similarity_search(self):
        self.initialize_vector_db()
        results = self.collection.query(query_embeddings=self.query_embeddings, n_results=3)
        self.retrieved_chunks = results["documents"][0]

    def query_result(self):
        self.query_retrieval()
        self.similarity_search()

        context = "\n".join(self.retrieved_chunks)

        prompt = f"""

        Answer only using the given context

        context: {context}

        Question: {self.user_query}

        """

        response = ollama.chat(model="llama3.2:3b",
                               messages=[
                                   {
                                       "role": "user",
                                       "content": prompt
                                   }
                               ]
                               )
        print(f"Answer: {response['message']['content']}")
