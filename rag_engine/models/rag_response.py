from dataclasses import dataclass
from .source_reference import SourceReference


@dataclass
class RAGResponse:
    answer: str
    sources: list[SourceReference]