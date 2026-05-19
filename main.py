from ingestion.data_ingestion import DataIngestion
from storage.storage import StoreEmbeddings


def main():
    emb = DataIngestion()
    emb.embedd_chunks(file_path="data/architecture_guide.pdf", chunk_size=500)
    store = StoreEmbeddings()
    store.store_embeddings_in_chromadb(emb.embeddings, emb.chunks)
    obj = QuerySearch("What are Embeddings?")
    obj.query_result()

if __name__ == "__main__":
    main()
