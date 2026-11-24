from langchain_community.document_loaders import DirectoryLoader, TextLoader

class DocumentLoader:

    def load_documents(self):

        loader = DirectoryLoader(
            "./dynamics365-docs/articles/commerce/b2b/",
            glob="*.md",
            loader_cls=TextLoader
        )

        documents = loader.load()

        for doc in documents:
            print(doc.metadata["source"])

        return documents