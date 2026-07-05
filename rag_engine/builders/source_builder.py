from rag_engine.models.source_reference import SourceReference
from langchain_core.documents import Document
class SourceBuilder:
    
    def build(documents: list[Document])-> list[SourceReference]:
        sources = []
        seen = set()

        for doc in documents:

            ref = SourceReference(
                source=doc.metadata.get("source", "Unknown"),
                page=doc.metadata.get("page", -1),
                content_type=doc.metadata.get("content_type", "text"),
            )

            key = (ref.source, ref.page, ref.content_type)

            if key not in seen:
                seen.add(key)
                sources.append(ref)

        return sources 
            
        