from pathlib import Path

from .base_loader import BaseLoader


class VideoLoader(BaseLoader):

    def load(self, source: str) -> Path:
        
        return Path(source)