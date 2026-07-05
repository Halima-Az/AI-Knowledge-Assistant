from dataclasses import dataclass


@dataclass(frozen=True)
class SourceReference:
    source: str
    page: int
    content_type: str