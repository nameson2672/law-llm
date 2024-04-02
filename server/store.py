# pinecone_utils.py

from pinecone import Pinecone
from langchain.embeddings.huggingface import HuggingFaceEmbeddings

class PineconeConnector:
    vectore_index=''
    pineconeinecone : Pinecone
    def __init__(self, api_key, index_name, dimension):
        self.pineconeinecone = Pinecone(api_key=api_key)
        self.vectore_index = self.pineconeinecone.Index(name=index_name, dimension=dimension)
    
    def index(self, index_name, dimension):
        self.vectore_index = self.pineconeinecone.Index(name=index_name, dimension=dimension)

    def upsert_embeddings(self, namespace, embeddings):
        self.vectore_index.upsert(namespace= namespace, vectors=embeddings)

    def query_similar_items(self, query_embedding, namespace='', top_k=2,include_metadata=True):
        return self.vectore_index.query(vector=query_embedding,top_k=top_k,
        include_values=False, namespace=namespace, include_metadata=include_metadata)
    
    def store_from_doc(self, docs, embedding_model):
        pass
