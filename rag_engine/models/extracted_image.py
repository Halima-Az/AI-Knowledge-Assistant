from dataclasses import dataclass

from PIL import Image


@dataclass(slots=True)
class ExtractedImage:
    """
    Représente une image extraite d'un PDF.
    """

    image: Image.Image

    page: int

    xref: int

    width: int

    height: int

    extension: str