import os
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from langchain_community.llms import HuggingFaceEndpoint
from langchain_core.prompts import ChatPromptTemplate
from langchain.memory import ConversationBufferMemory
from langchain.chains.llm import LLMChain
from langchain.prompts.chat import ChatPromptTemplate, HumanMessagePromptTemplate, MessagesPlaceholder
from langchain_core.messages import SystemMessage
import spacy


app = FastAPI()

origins = ["*"]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


nlp = spacy.load("en_core_web_sm")

# template_messages = [
#     SystemMessage(content="You are a helpful assistant."),
#     MessagesPlaceholder(variable_name="chat_history"),
#     HumanMessagePromptTemplate.from_template("{text}"),
# ]
# prompt_template = ChatPromptTemplate.from_messages(template_messages)

# llm = HuggingFaceEndpoint(
#     inference_server_url="http://127.0.0.1:8080/",
#     max_new_tokens=512,
#     top_k=50,
#     temperature=0.1,
#     repetition_penalty=1.03
# )

# model = Llama2Chat(llm)
# memory = ConversationBufferMemory(memory_key="chat_history", return_messages=True)
# chain = LLMChain(llm=model, prompt=prompt_template, memory=memory)



@app.post("/chat/")
async def quick_response(msg: str):
    doc = nlp(msg)
    query = ""
    for token in doc:
        cur = token.text+ " " + token.pos_ + " "+ token.tag_ + " "
        query = query + cur 
    print(query)
    return query
