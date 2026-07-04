
import os

from dotenv import load_dotenv

from langchain_ollama import ChatOllama


load_dotenv()


class LLMProvider:

    def __init__(self):

        self.llm = ChatOllama(

            model="gemma3:4b",

            temperature=0
        )

    def get_llm(self):

        return self.llm