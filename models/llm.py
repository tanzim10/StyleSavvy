
from transformers import pipeline
from typing import List

PROMPTS = {
    "category_expansion": (
        "As a top-tier fashion advisor, craft one impactful styling suggestion for a {gender} individual with a {body_type} body "
        "and {face_shape} face attending the {occasion}. They have on {items}. "
        "Highlight a strategic enhancement in silhouette, color scheme, accessory choice, or footwear to elevate their look."
    ),
    "event_aesthetic": (
        "Imagine you are curating an immersive style experience for a {gender} attendee with a {body_type} silhouette and {face_shape} face at the {occasion}. "
        "They’re currently wearing {items}. Provide one highly descriptive recommendation that harmonizes fabric textures, color temperature, silhouette, and accessory accents with the event’s specific ambiance, lighting conditions, and seasonal atmosphere."
    ),
    "fashion_editor": (
        "You are the Editor-in-Chief of a prestigious fashion publication. Advise a {gender} trendsetter with a {body_type} frame and {face_shape} face attending the {occasion}, "
        "currently in {items}. Offer one magazine-cover-worthy styling tip—highlight a trending color palette, editorial-worthy silhouette, and innovative accessory placement that will resonate with a discerning audience."
    ),
    "influencer_style": (
        "As a cutting-edge style influencer with millions of followers, recommend one eye-catching flair tip for a {gender} follower with a {body_type} physique and {face_shape} face, "
        "heading to the {occasion} in {items}. Frame it as a social-media-caption-ready moment: mention a statement accessory, bold color pop, or texture twist that will go viral."
    ),
    "seasonal_trend": (
        "As a seasonal style expert specializing in spring/summer trends, guide a {gender} individual with a {body_type} shape and {face_shape} face preparing for the {occasion}. "
        "They currently wear {items}. Provide one tip incorporating current seasonal motifs—think floral prints, breathable linens, or eco-friendly fabrics—that elevates their ensemble."
    ),
}

class StyleSavvy:
    def __init__(
        self,
        model_name: str = "google/flan-t5-large",
        device: int   = -1,     # -1 = CPU, or GPU index
        max_length: int = 150,
    ):
        # A local instruction-tuned T5 model
        self.pipe = pipeline(
            "text2text-generation",
            model=model_name,
            tokenizer=model_name,
            device=device,
        )
        self.max_length = max_length
        self.num_beams = 4
    # TODO: Modification: Add more prompts to the advise function
    # to make it more specific to the user's needs.
    # The function now takes in the user's body type, face shape, and occasion
    # and generates style tips accordingly.

    def advise(self,
               items: List[str],
               body_type: str,
               face_shape: str,
               gender: str,
               occasion: str
    ) -> List[str]:
        """
        Generate one result per prompt template and return all as a list.
        """
        labels = ", ".join(items) if items else "an outfit"
        results: List[str] = []
        for tpl in PROMPTS.values():
            prompt = tpl.format(
                body_type=body_type,
                face_shape=face_shape,
                gender = gender,
                occasion=occasion,
                items=labels
            )
            out = self.pipe(
                prompt,
                max_length=self.max_length,
                num_beams=self.num_beams,
                early_stopping=True,
                do_sample=False,
                no_repeat_ngram_size=3,  # avoid repeating phrases
            )[0]["generated_text"].strip()
            results.append(out)
        return results




