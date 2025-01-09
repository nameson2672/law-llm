# Legal Assistance AI - RAG Architecture

This repository contains the codebase for a Legal Assistance AI application built on the Retrieval-Augmented Generation (RAG) architecture. The app is designed to help individuals resolve legal issues by suggesting actionable solutions, referencing relevant laws, and providing insights based on past cases with similar issues. 

## Key Features

1. **Legal Query Assistance**: Users can input queries about legal issues, and the app provides actionable suggestions.
2. **Law Section References**: The app highlights the relevant legal sections and guidelines applicable to the user’s query.
3. **Past Case Insights**: Provides information on how similar cases were resolved, offering users a deeper understanding of their situation.
4. **Powered by RAG Architecture**: Combines local vector search and context-enhanced queries with a Large Language Model (LLM) to provide accurate and human-like responses.

---

## System Architecture

### Overview
The system is based on the Retrieval-Augmented Generation (RAG) architecture and consists of the following components:

1. **Client Location**:
   - **AI Engineer**: Prepares and ingests client data for processing.
   - **Client Data & Data Processing**: Processes the data to generate embeddings.
   - **Vector Database**: Stores the embeddings to enable efficient search.

2. **Cloud (SaaS) or On-premises**:
   - **GenAI App**: Handles user queries, searches for relevant data, and sends context-enhanced queries to the LLM.
   - **Large Language Model (LLM)**: Provides human-like responses and generates insights based on the provided context.

![System Architecture](https://raw.githubusercontent.com/nameson2672/law-llm/refs/heads/main/static/system-architecture.png)

### Workflow
1. **Data Preparation**: Client data is ingested and processed to generate embeddings.
2. **Embedding Generation**: Data embeddings are created using the chosen model and stored in a vector database.
3. **Vector Search**: When a user submits a query, the app searches for relevant information in the vector database.
4. **Enhanced Querying**: The retrieved data is used to enhance the query, which is sent to the LLM.
5. **Response Generation**: The LLM generates a human-like response based on the enhanced context, which is returned to the user.

---

## Running the App Locally

### Prerequisites
1. **Get Access to Llama2 LLM**:
   - Sign up for [Meta Llama2 LLM](https://llama.meta.com/llama-downloads) and [HuggingFace](https://huggingface.co/login) using the same email.
   - Obtain access to the Llama2 LLM.

2. **Download Llama2 7B Chat Model**:
   - Create a folder called `Models` inside the `server` directory.
   - Download the [Llama2 7B Chat Model](https://huggingface.co/meta-llama/Llama-2-7b-chat-hf) and place it in the `Models` folder.

### Setting Up the Environment
1. Install the required dependencies using pip:
   ```bash
   pip install "uvicorn[standard]"
   ```
2. Start the server:
   ```bash
   uvicorn main:app --reload
   ```

---

## Directory Structure
```
.
├── server
│   ├── Models
│   │   └── Llama-2-7b-chat-hf
│   ├── main.py
│   └── ...
├── client
│   ├── index.html
│   ├── styles.css
│   └── app.js
└── README.md
```

### Key Files
- `main.py`: Contains the backend logic for processing queries and communicating with the LLM.
- `Models`: Directory for storing the Llama2 model.
- `client`: Contains the frontend files (HTML, CSS, and JavaScript).

---

## Dependencies
- Python 3.8+
- [Uvicorn](https://www.uvicorn.org/)
- Llama2 7B Chat Model

---

## Usage
1. Run the server using the instructions above.
2. Access the app through the local development server.
3. Input legal queries and get actionable solutions, case references, and law sections.

---

## Contributing
We welcome contributions to improve this Legal Assistance AI app. Please follow these steps:
1. Fork the repository.
2. Create a new branch for your feature or bug fix.
3. Submit a pull request with a detailed explanation of your changes.

---

## License
This project is licensed under the MIT License. See the LICENSE file for details.

---

## Acknowledgments
- **Meta Llama2** for providing the base language model.
- The open-source community for tools and libraries.

---

Start using the Legal Assistance AI app to resolve your legal queries efficiently and effectively!