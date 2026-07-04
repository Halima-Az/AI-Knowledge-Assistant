import base64
import io
from PIL import Image


def image_to_base64(image: Image.Image) -> str:
    """
    Convertit une image PIL en chaîne Base64.
    """

    buffer = io.BytesIO()

    image.save(buffer, format="PNG")

    return base64.b64encode(buffer.getvalue()).decode("utf-8")