import os, requests
from io import BytesIO
from PIL import Image
from dotenv import load_dotenv

load_dotenv()

API_KEY = os.getenv("REMOVE_BG_API_KEY")
ENDPOINT = "https://api.remove.bg/v1.0/removebg"

def remove_background(image_bytes: bytes) -> Image.Image:
    resp = requests.post(
        ENDPOINT,
        files ={"image_file": ("image.jpg", image_bytes, "image/jpeg")},
        data = {"size": "auto"},
        headers = {"X-Api-Key": API_KEY},
    )
    resp.raise_for_status()
    return Image.open(BytesIO(resp.content))

