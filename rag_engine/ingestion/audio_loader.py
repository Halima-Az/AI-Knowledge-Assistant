from pathlib import Path

from .base_loader import BaseLoader


class AudioLoader(BaseLoader):

    def load(self, source: str) -> Path:
        
        return Path(source)