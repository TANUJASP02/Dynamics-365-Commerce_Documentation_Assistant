from langchain_classic.chains.combine_documents import create_stuff_documents_chain
from langchain_classic.chains import create_retrieval_chain

class RAGChain:

    def create_rag_chain(self, retriever, llm, prompt):

        document_chain = create_stuff_documents_chain(llm, prompt)

        retrieval_chain = create_retrieval_chain(retriever, document_chain)

        return retrieval_chain