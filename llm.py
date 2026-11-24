from langchain_ollama import OllamaLLM


class LLM:

    def create_llm(self):

        llm_model = "gpt-oss:20b"
        ollama_url = "https://browsing-change-broaden.ngrok-free.dev"

        llm = OllamaLLM(model=llm_model, base_url=ollama_url, temperature=0)

        return llm
