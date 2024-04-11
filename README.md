# Law Llm

## Running App locally

### Get access to Lama2 llm

Signe up for Meta Lama2 LLM and Huggingface with same email and Get access to LLm

Meta LLM: https://llama.meta.com/llama-downloads
HuggingFace: https://huggingface.co/login

### Setting Up environment:
First of all create folder called `Models` inside `server` and place 7b llama2 LLM in place.
Downlode From : https://huggingface.co/meta-llama/Llama-2-7b-chat-hf
and the install dependency for the app using `pip` and start server using following command:

```bash
pip install "uvicorn[standard]"
uvicorn main:app --reload
```