# from sentence_transformers import SentenceTransformer
#
# # Function will load the embedding modal
# def load_embedding_modal():
#     embedding_model = SentenceTransformer(
#         "all-MiniLM-L6-v2"
#     )
#     print("Embedding modal loaded")
#     return embedding_model
#
#
# # Function will convert the chunks into embeddings
# def get_embedding(chunks):
#     load_embedding_modal()
#     embedding = load_embedding_modal().encode(chunks).tolist()
#     return embedding