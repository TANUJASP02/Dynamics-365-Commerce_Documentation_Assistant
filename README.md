Dynamics 365 Commerce Documentation Assistant

Project Overview

An AI-powered documentation assistant designed to answer questions related to Microsoft Dynamics 365 Commerce. The application uses Retrieval-Augmented Generation (RAG) to retrieve relevant information from official Microsoft documentation and generate context-based answers.

Technologies Used

- Python
- LangChain
- Retrieval-Augmented Generation (RAG)
- ChromaDB
- Ollama
- Nomic Embed Text
- Streamlit

Project Workflow

1. Document Collection: Retrieves Dynamics 365 Commerce documentation from GitHub.
2. Text Splitting: Splits documents into smaller chunks for efficient retrieval.
3. Embedding Generation: Uses the Nomic Embed Text model to convert text into vector embeddings.
4. Vector Database: Stores document embeddings in ChromaDB.
5. User Query: Accepts questions through the Streamlit interface.
6. Query Rewriting: Improves ambiguous or indirect questions before retrieval.
7. Context Retrieval: Retrieves relevant document chunks from ChromaDB.
8. LLM Response: Uses Ollama to generate answers based on the retrieved context.

Key Features

- AI-powered question answering.
- Retrieval-Augmented Generation (RAG).
- Automatic document retrieval from GitHub.
- Semantic search using vector embeddings.
- Query rewriting for better retrieval.
- Context-based answers from documentation.
- Streamlit user interface.

Architecture

User Question → Query Rewriting → Document Retrieval → ChromaDB → Retrieved Context → Ollama LLM → Final Answer

Project Objective

To simplify access to Dynamics 365 Commerce technical documentation by providing accurate, context-based answers through an AI-powered assistant.
