# test_detector.py

from detector import detect_clothing
from PIL import Image, ImageDraw
import os

def visualize_and_print(image_path, do_bg_remove=False, output_dir="vis"):
    # Ensure output folder exists
    os.makedirs(output_dir, exist_ok=True)

    img = Image.open(image_path).convert("RGB")
    print(f"\n--- Testing {os.path.basename(image_path)} (bg_remove={do_bg_remove}) ---")
    
    # Run your detector
    dets = detect_clothing(img, do_bg_remove=do_bg_remove)
    if not dets:
        print("No detections!")
        return

    # Print raw detections
    # Print raw detections
    for i, d in enumerate(dets.values(), 1):
        lbl = d["label"]
        scr = d["score"]
        box = d.get("box", [])
        print(f" {i}. {lbl:12s} @ {scr:.2f} → {box}")

    # Draw boxes
    vis = img.copy()
    draw = ImageDraw.Draw(vis)
    for d in dets.values():
        if d.get("box"):
            x0, y0, x1, y1 = d["box"]
            draw.rectangle([x0, y0, x1, y1], outline="red", width=2)
            draw.text((x0, y0 - 10), f"{d['label']}:{d['score']:.2f}", fill="red")
        # Save visualization
        out_path = os.path.join(output_dir, os.path.basename(image_path))
        vis.save(out_path)
        print(f" Visualization saved to {out_path}")
    
if __name__ == "__main__":
    # List your test images here
    samples = [
        "/Users/tanzimfarhan/Desktop/Python/Codes/SLU/CS5930/FinalProject/StyleSavvy/images/casual.jpg",
        "/Users/tanzimfarhan/Desktop/Python/Codes/SLU/CS5930/FinalProject/StyleSavvy/images/WomenCasual.jpg",
    ]
    for img_path in samples:
        visualize_and_print(img_path, do_bg_remove=False)
        # visualize_and_print(img_path, do_bg_remove=True)
