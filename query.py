import ollama

from embedding import load_embedding_modal
from storage import initialize_chromadb

class QuerySearch:

    def __init__(self, user_query):
        self.query_embeddings = None
        self.retrieved_chunks = None
        self.user_query = user_query

    def query_retrieval(self):
        embedding_modal = load_embedding_modal()
        self.query_embeddings = embedding_modal.encode(self.user_query).tolist()

    def similarity_search(self):
        collection = initialize_chromadb()
        results = collection.query(query_embeddings=self.query_embeddings, n_results=3)
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

        response = ollama.chat(model="llama3:8B",
                               messages = [
                                   {
                                       "role": "user",
                                       "content": prompt
                                   }
                               ]
                            )
        print(response["messages"]["content"])