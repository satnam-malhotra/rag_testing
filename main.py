from ingestion.data_embedding import DataEmbedding
from agents.query import QuerySearch
from storage.storage import StoreEmbeddings


def main():
    emb = DataEmbedding(chunk_size=500, file_path="data/architecture_guide.pdf")
    emb.embedd_chunks()
    embeddings = emb.embeddings
    chunks = emb.chunks
    store = StoreEmbeddings()
    store.store_embeddings_in_chromadb(embeddings, chunks)
    obj = QuerySearch("What are Embeddings?")
    obj.query_result()

if __name__ == "__main__":
    main()
