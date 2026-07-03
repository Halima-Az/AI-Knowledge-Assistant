
from langchain_core.prompts import ChatPromptTemplate


class PromptBuilder:

    def __init__(self):

        self.prompt = ChatPromptTemplate.from_template(
            """
                Tu es un assistant IA.

                Réponds uniquement à partir du contexte.

                Si l'information n'est pas présente,
                réponds :
                "Je ne trouve pas cette information dans les documents."

                Contexte :

                {context}

                Question :

                {question}

                Réponse :
                """
        )

    def get_prompt(self):

        return self.prompt