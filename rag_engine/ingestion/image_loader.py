from PIL import Image

from .base_loader import BaseLoader


class ImageLoader(BaseLoader):

    def load(self, source: str) -> Image.Image:
       
        return Image.open(source)