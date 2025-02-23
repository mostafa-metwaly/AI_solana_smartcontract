import base64
from io import BytesIO


def encode_image_to_base64(image_path: str):
    """
    Reads an image file and encodes it as a base64 string.
    
    Parameters:
    - image_path (str): Path to the image file.

    Returns:
    - str: Base64-encoded string of the image.
    """
    with open(image_path, "rb") as image_file:
        return base64.b64encode(image_file.read()).decode("utf-8")


def decode_base64_to_bytes(encoded_str: str):
    return BytesIO(base64.b64decode(encoded_str))

def encode_bytes_to_base64(bytes):
    return base64.b64encode(bytes).decode("utf-8")
