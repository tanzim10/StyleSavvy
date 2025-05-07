
# models/vision.py -- Working

from transformers import pipeline
from PIL import Image

class VisionModel:
    def __init__(
        self,
        model_name: str = "valentinafeve/yolos-fashionpedia",
        threshold: float = 0.7
    ):
        self.pipe = pipeline("object-detection", model=model_name)
        self.threshold = threshold

    def detect(self, image: Image.Image):
        # 1) Ensure RGB
        if image.mode != "RGB":
            image = image.convert("RGB")

        # 2) Run detection
        results = self.pipe(image)

        # 3) Process & filter
        processed = []
        for r in results:
            score = float(r["score"])
            if score < self.threshold:
                continue

            # r["box"] is a dict: {"xmin":..., "ymin":..., "xmax":..., "ymax":...}
            box = r["box"]
            coords = [
                float(box["xmin"]),
                float(box["ymin"]),
                float(box["xmax"]),
                float(box["ymax"]),
            ]

            processed.append({
                "label": r["label"],
                "score": score,
                "box": coords
            })

        return processed




