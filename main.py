from query import QuerySearch
from storage import generate_and_store_embedding

def main():
    obj = QuerySearch("What are Embeddings?")
    obj.query_result()

if __name__ == "__main__":
    generate_and_store_embedding()
    main()
