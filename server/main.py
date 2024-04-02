import os
from typing import List
import uuid
from fastapi import File, UploadFile
from fastapi import FastAPI, UploadFile
from fastapi.middleware.cors import CORSMiddleware
from sklearn.base import TransformerMixin
import spacy
from langchain.prompts import PromptTemplate
from langchain_community.llms import CTransformers
from embed import EmbeddingGenerator
from store import PineconeConnector


UPLOAD_DIRECTORY = "data"  # Directory to store uploaded files

if not os.path.exists(UPLOAD_DIRECTORY):
    os.makedirs(UPLOAD_DIRECTORY)

app = FastAPI()

origins = ["*"]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Create index in Pinecone
index_name = "lawllm"
dimension = 768  # Dimension of Hugging Face embeddings

# Initialize Pinecone connector
pinecone_store = PineconeConnector(api_key="f2761cc2-2b0e-4179-8967-cd6f36b73be2", index_name=index_name, dimension=dimension)

# Initialize embedding generator
embedding_generator = EmbeddingGenerator(model_name="all-MiniLM-L6-v2")



nlp = spacy.load("en_core_web_sm")


### LLama2 model
llm=CTransformers(model='Models/llama-2-7b-chat.Q2_K.gguf',
                      model_type='llama',
                      config={'max_new_tokens':256,
                              'temperature':0.8, 'gpu_layers':1000})
template="""
        Answer the following QUESTION based on the CONTEXT
given. If you do not know the answer and the CONTEXT doesn't
contain the answer truthfully say "I don't know". And answer in an Html code formate
CONTEXT: {context} 
QUESTION: {question}.
"""
    
prompt=PromptTemplate(input_variables=["context","question"],
                          template=template)



@app.post("/chat/")
async def chat(msg: str):
    doc = nlp(msg)
    query = ""
    for token in doc:
        cur = token.text+ " " + token.pos_ + " "+ token.tag_ + " "
        query = query + cur 
    print(query)
    input_text = msg
    no_words ="300"
    blog_style = "Technical"
    query_embeding = embedding_generator.embed_query(msg)
    data = pinecone_store.query_similar_items(query_embedding=query_embeding)
    contexts = [match.metadata["text"] for match in data.matches]
    print(contexts)
    context_str = construct_context(contexts=contexts)

    return llm(prompt.format(context=context_str,question=msg))

@app.post("/upload/")
async def upload_file(file: UploadFile = File(...)):
    # Get a unique filename for the uploaded file
    unique_filename = get_unique_filename(file.filename)
    file_path = os.path.join(UPLOAD_DIRECTORY, unique_filename)
    
    # Write the uploaded file to the specified file path
    with open(file_path, "wb") as buffer:
        buffer.write(await file.read())
    
    # Return the unique filename
    return {"filename": unique_filename, "path": file_path}

@app.post("/convert-embed/")
async def embed_doc(files: List[UploadFile] = File(...)):

    pass


def get_unique_filename(filename):
    # Generate a unique filename using UUID
    unique_filename = str(uuid.uuid4()) + os.path.splitext(filename)[1]
    return unique_filename



def construct_context(contexts: List[str]) -> str:
    chosen_sections = []
    chosen_sections_len = 0
    max_section_len = 1000
    separator = "\n"

    for text in contexts:
        text = text.strip()
        # Add contexts until we run out of space.
        chosen_sections_len += len(text) + 2
        if chosen_sections_len > max_section_len:
            break
        chosen_sections.append(text)
    concatenated_doc = separator.join(chosen_sections)
    return concatenated_doc