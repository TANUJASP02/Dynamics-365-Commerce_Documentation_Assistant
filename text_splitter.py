import re

from langchain_core.documents import Document
from langchain_text_splitters import RecursiveCharacterTextSplitter


class TextSplitter:

    def split_documents(self, documents):

        final_chunks = []

        splitter = RecursiveCharacterTextSplitter(
            chunk_size=2500,
            chunk_overlap=500
        )

        for document in documents:

            # Get the full document text
            text = document.page_content

            # Find headings like ## Heading
            parts = re.split(r"(?m)^(#{1,3})\s+(.+)$", text)

            # Go through each section
            for i in range(1, len(parts), 3):

                heading = parts[i + 1].strip()
                content = parts[i + 2].strip()

                if not content:
                    continue

                # Keep heading + content together
                section = heading + "\n\n" + content

                # Split only if section is too large
                if len(section) > 2500:

                    small_chunks = splitter.split_text(section)

                    for chunk in small_chunks:
                        final_chunks.append(
                            Document(
                                page_content=chunk,
                                metadata=document.metadata.copy()
                            )
                        )

                else:

                    final_chunks.append(
                        Document(
                            page_content=section,
                            metadata=document.metadata.copy()
                        )
                    )

        return final_chunks