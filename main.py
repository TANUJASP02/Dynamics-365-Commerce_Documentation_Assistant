import asyncio
from connector import RAGConnector


async def main():

    connector_obj = RAGConnector()

    await connector_obj.initialize()

    question = input("\nEnter your question: ")

    answer = await connector_obj.ask_question(question)

    print("\nANSWER")
    print(answer)


if __name__ == "__main__":
    asyncio.run(main())