import io
import fitz

from PIL import Image

from rag_engine.extractors.base_extractor import BaseExtractor
from rag_engine.models.extracted_image import ExtractedImage


class PDFImageExtractor(BaseExtractor):
    """
    Extrait toutes les images d'un document PDF.
    """

    def extract(self, pdf: fitz.Document) -> list[ExtractedImage]:

        extracted_images = []

        for page_number, page in enumerate(pdf, start=1):

            images = page.get_images(full=True)

            for image in images:

                xref = image[0]

                image_info = pdf.extract_image(xref)

                image_bytes = image_info["image"]

                pil_image = Image.open(io.BytesIO(image_bytes))

                extracted_images.append(

                    ExtractedImage(

                        image=pil_image,

                        page=page_number,

                        xref=xref,

                        width=image_info["width"],

                        height=image_info["height"],

                        extension=image_info["ext"]

                    )

                )

        return extracted_images