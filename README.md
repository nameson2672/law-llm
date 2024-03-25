# Law Llm

## Running App locally
First of all create folder called `Models` inside `server` and place 7b llama2 LLM in place.

and the install dependency for the app using `pip` and start server using following command:

```bash
pip install "uvicorn[standard]"
uvicorn main:app --reload
```