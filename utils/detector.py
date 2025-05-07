
from io import BytesIO
from PIL import Image
from models.vision import VisionModel
from utils.bg_removal import remove_background

vision = VisionModel()
FASHION_LABELS = {
    "shirt", "t-shirt", "blouse", "tank top", "sweater", "hoodie", "jacket",
    "coat", "overcoat", "raincoat", "windbreaker", "cardigan", "blazer",
    "pants", "jeans", "shorts", "leggings", "tights", "skirt", "dress",
    "suit", "jumpsuit", "romper", "vest", "sports bra", "tracksuit",
    "belt", "tie", "scarf", "hat", "cap", "gloves", "socks",
    "shoe", "sneakers", "boots", "sandals", "heels",
    "watch", "necklace", "bracelet", "earrings", "ring",
    "backpack", "handbag", "purse", "wallet"
}

def detect_clothing(image_input, do_bg_remove: bool = False):
    # 1) Load into a PIL.Image if it's a filepath
    if isinstance(image_input, str):
        img = Image.open(image_input)
    else:
        img = image_input

    # 2) Optionally remove background (works on bytes)
    if do_bg_remove:
        buf = BytesIO()
        img.convert("RGB").save(buf, format="JPEG")
        img_bytes = buf.getvalue()
        img = remove_background(img_bytes)
    else:
        # ensure you drop any alpha channel
        img = img.convert("RGB")

    # 3) Run detection
    raw_detections = vision.detect(img)

    # 4) Filter and deduplicate
    filtered = {}
    for det in raw_detections:
        label = det["label"].lower()
        if label in FASHION_LABELS:
            # Only keep the first or highest score if multiple detected
            if label not in filtered or det["score"] > filtered[label]["score"]:
                filtered[label] = {
                    "label": label,
                    "score": det["score"],
                    "box": det.get("box", [])
                }

    # 5) Return dict or fallback if empty
    if not filtered:
        return {"outfit": {"label": "outfit", "score": 1.0, "box": []}}

    return filtered



