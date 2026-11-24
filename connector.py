from document_loader import DocumentLoader
from text_splitter import TextSplitter
from embeddings import Embeddings
from chroma_store import ChromaStore
from retriever import Retriever
from llm import LLM
from prompt import Prompt
from chains import RAGChain


class RAGConnector:
    def __init__(self):
        self.retrieval_chain = None

    async def initialize(self):
        documentloader_obj = DocumentLoader()
        textsplitter_obj = TextSplitter()
        embeddingsmodel_obj = Embeddings()
        chromastore_obj = ChromaStore()
        retriever_obj = Retriever()
        llm_obj = LLM()
        prompt_obj = Prompt()
        ragchain_obj = RAGChain()

        documents = documentloader_obj.load_documents()
        print("Documents loaded:", len(documents))

        chunks = textsplitter_obj.split_documents(documents)
        print("Chunks created:", len(chunks))

        embeddings = embeddingsmodel_obj.create_embeddings()
        print("Embeddings model created")

        vectorstore = chromastore_obj.create_vectorstore(
            chunks,
            embeddings,
        )
        print("Documents stored in ChromaDB")

        retriever = retriever_obj.create_retriever(vectorstore)
        print("Retriever created")

        llm = llm_obj.create_llm()
        print("LLM created")

        prompt = prompt_obj.create_prompt()

        self.retrieval_chain = ragchain_obj.create_rag_chain(
            retriever,
            llm,
            prompt,
        )
        print("RAG chain created")

    def format_history(self, chat_history):
        if not chat_history:
            return ""

        history_lines = []

        for message in chat_history:
            role = message.get("role", "")
            content = message.get("content", "").strip()

            if not content:
                continue

            if role == "user":
                history_lines.append(f"User: {content}")

            elif role == "assistant":
                history_lines.append(f"Assistant: {content}")

        return "\n".join(history_lines)

    async def ask_question(self, question, chat_history=None):
        if self.retrieval_chain is None:
            raise ValueError("RAG chain is not initialized.")

        history = self.format_history(chat_history)

        if history:
            rag_question = (
                "Conversation history:\n"
                f"{history}\n\n"
                "Current question:\n"
                f"{question}"
            )
        else:
            rag_question = question

        result = self.retrieval_chain.invoke(
            {
                "input": rag_question,
            }
        )

        answer = result.get(
            "answer",
            "I could not generate an answer.",
        )

        return {
            "answer": answer,
            "context": result.get("context", []),
        }