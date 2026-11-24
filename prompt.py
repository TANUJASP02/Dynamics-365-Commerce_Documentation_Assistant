from langchain_core.prompts import ChatPromptTemplate


class Prompt:

    def create_prompt(self):

        prompt = ChatPromptTemplate.from_template("""
Use only the provided context to answer the question.

Instructions:
Find the section in the context that best matches the question.
Return the complete matching section.
Copy the content from the context without paraphrasing.
Do not summarize.
Do not skip any part of the matching section.
Do not add information that is not in the context.
Preserve the original order.
For numbered lists, convert repeated numbering such as 1., 1., 1. into sequential numbering: 1., 2., 3., 4., etc.

If the answer is not available in the context, say:
"I can only answer questions related to the provided documents."

Context:
{context}

Question:
{input}

Answer:
""")

        return prompt