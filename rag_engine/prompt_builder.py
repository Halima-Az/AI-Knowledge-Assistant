from langchain_core.prompts import ChatPromptTemplate


class PromptBuilder:

    def __init__(self):

        self.prompt = ChatPromptTemplate.from_messages(
            [
                (
                    "system",
                    """
                    You are an AI assistant specialized in question answering over retrieved documents.

                    Rules:

                    1. Answer ONLY using the provided context.

                    2. The context may contain:
                    - plain text
                    - tables
                    - charts
                    - image descriptions
                    - OCR results

                    3. If the answer exists in the context, answer clearly and naturally.

                    4. If the context contains a table, use its values.

                    5. If the context contains an image description, use it.

                    6. If the answer is not explicitly present but can be reasonably inferred from the context, mention that it is an estimation.

                    7. If the answer truly cannot be found, reply only:

                    "I couldn't find this information in the provided documents."

                    Do not invent facts.
                                        """
                                    ),
                                    (
                                        "human",
                                        """
                    Context:

                    {context}


                    Question:

                    {question}
                    """
                )
            ]
        )

    def get_prompt(self):
        return self.prompt