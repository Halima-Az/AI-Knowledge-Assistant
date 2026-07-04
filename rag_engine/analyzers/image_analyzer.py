from langchain_core.documents import Document
from langchain_core.messages import HumanMessage

from rag_engine.models.extracted_image import ExtractedImage
from rag_engine.llm import LLMProvider
from rag_engine.tools.image_utils import image_to_base64


class ImageAnalyzer:

    def __init__(self):
        self.llm = LLMProvider().get_llm()

    def analyze(self, extracted_image: ExtractedImage) -> Document:

        image_b64 = image_to_base64(extracted_image.image)

        message = HumanMessage(
            content=[
                {
                    "type": "text",
                    "text": (
                        "Analyze this image extracted from a PDF. "
                        "Describe diagrams, charts, tables, visible text "
                        "and all important information."
                    ),
                },
                {
                    "type": "image_url",
                    "image_url": f"data:image/png;base64,{image_b64}",
                },
            ]
        )

        response = self.llm.invoke([message])

        return Document(
            page_content=response.content,
            metadata={
                "source": "image",
                "page": extracted_image.page,
                "content_type": "image",
            },
        )