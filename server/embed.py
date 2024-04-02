from langchain.embeddings.huggingface import HuggingFaceEmbeddings
from langchain_text_splitters import CharacterTextSplitter
from langchain_community.document_loaders import PyPDFLoader

def get_embedding_model(embedding_model_name, model_kwargs, encode_kwargs):
    
    embedding_model = HuggingFaceEmbeddings(
            model_name=embedding_model_name,
            model_kwargs=model_kwargs,
            encode_kwargs=encode_kwargs,
        )
    return embedding_model

class EmbeddingGenerator:
    def __init__(self, model_name):
        # Embedding model
        self.embedding_model = get_embedding_model(
            embedding_model_name=model_name,
            model_kwargs={"device": "cuda"},
            encode_kwargs={"device": "cuda", "batch_size": 100},
        )
        
    def embed_query(self,query:str):
        return self.embedding_model.embed_query(query)
    
    def __call__(self, batch):
        embeddings = self.embedding_model.embed_documents(batch=batch)
        return {"text": batch["text"], "source": batch["source"], "embeddings": embeddings}