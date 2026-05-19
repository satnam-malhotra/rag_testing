# import pymupdf
#
# # Function to read the files and convert it into equal chunks
# def read_chunks():
#     doc = pymupdf.open("data/architecture_guide.pdf")
#     text = ""
#     for page in doc:
#         text += page.get_text()
#     chunk_size = 500
#     chunks = []
#     for i in range(0, len(text), chunk_size):
#         chunks.append(text[i:i+chunk_size])
#     return chunks