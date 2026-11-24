from langchain_chroma import Chroma
import shutil
import os


class ChromaStore:

    def create_vectorstore(self, chunks, embeddings):

        if os.path.exists("./chroma_db"):
            shutil.rmtree("./chroma_db")

        vectorstore = Chroma.from_documents(
            documents=chunks,
            embedding=embeddings,
            persist_directory="./chroma_db"
        )

        return vectorstore