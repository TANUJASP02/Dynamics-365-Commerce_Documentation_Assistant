class Retriever:

    def create_retriever(self, vectorstore):

        retriever = vectorstore.as_retriever(
            search_kwargs={"k": 5}
        )

        return retriever