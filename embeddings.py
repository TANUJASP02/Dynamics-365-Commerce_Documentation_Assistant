from langchain_ollama import OllamaEmbeddings


class Embeddings:

    def create_embeddings(self):

        embedding_model = "nomic-embed-text"
        ollama_url = "https://browsing-change-broaden.ngrok-free.dev"

        embeddings = OllamaEmbeddings(model=embedding_model, base_url=ollama_url)

        return embeddings