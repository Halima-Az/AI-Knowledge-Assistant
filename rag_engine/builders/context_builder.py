from langchain_core.documents import Document


class ContextBuilder:

    def build(self, docs: list[Document]) -> str:

        context = []

        for doc in docs:

            source = doc.metadata.get("source", "Unknown")
            page = doc.metadata.get("page", "?")
            content_type = doc.metadata.get("content_type", "text")

            context.append(
                f"""
                    Source: {source}
                    Page: {page}
                    Type: {content_type}

                    {doc.page_content}
                """
            )

        return "\n\n------------------------------\n\n".join(context)