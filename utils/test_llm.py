# # test_llm.py
# """
# Test harness for StyleSavvy LLM prompts.
# Defines multiple prompt templates and evaluates the generated outputs,
# checking for the expected number of bullet-point style tips.
# """
# from models.llm import StyleSavvy

# # Variant prompt templates with placeholders
# PROMPT_TEMPLATES = {
#     "occasion_driven": (
#         "You are an expert fashion stylist. A client is preparing for {occasion}. "
#         "They have a {body_type}-shaped body and a {face_shape} face. They’re currently wearing: {items}. "
#         "Give 3 to 5 *distinct* style tips focused on making them look their best at the event. "
#         "Make the suggestions relevant to the setting, weather, and formality of the occasion. "
#         "Avoid repeating any advice."
#     ),

#     "function_based": (
#         "You're advising someone with a {body_type} build and {face_shape} face. "
#         "They're attending a {occasion} and are wearing {items}. "
#         "Suggest 3–5 concise fashion improvements or enhancements. "
#         "Each suggestion should be unique and tailored to the event. "
#         "Include practical choices for color, layering, accessories, or footwear. "
#         "Avoid repeating words or phrases."
#     ),

#     "intent_style": (
#         "Act as a high-end personal stylist. Your client has a {body_type} body shape and a {face_shape} face. "
#         "They're going to a {occasion} and are wearing {items}. "
#         "Write 3 to 5 brief but powerful styling suggestions to elevate their look. "
#         "Focus on intent—what feeling or impression each style choice creates for the event."
#     ),
# }


# # Test parameters
# BODY_TYPE = "Slim"
# FACE_SHAPE = "Round"
# OCCASION = "Rooftop Evening Party"
# ITEMS = ["shirt", "jeans", "jacket","shoes"]

# if __name__ == "__main__":
#     advisor = StyleSavvy()

#     for name, template in PROMPT_TEMPLATES.items():
#         # Build prompt by replacing placeholders
#         prompt = template.format(
#             body_type=BODY_TYPE,
#             face_shape=FACE_SHAPE,
#             occasion=OCCASION,
#             items=", ".join(ITEMS)
#         )
#         print(f"=== Testing template: {name} ===")
#         print("Prompt:")
#         print(prompt)

#         # Generate output (use only supported args)
#         result = advisor.pipe(
#             prompt,
#             max_length=advisor.max_length,
#             early_stopping=True,
#             do_sample=False
#         )[0]["generated_text"].strip()

#         print("Generated output:")
#         print(result)

#         # Extract bullet lines
#         bullets = [ln for ln in result.splitlines() if ln.strip().startswith("- ")]
#         print(f"Number of bullets detected: {len(bullets)}")
#         for i, b in enumerate(bullets, start=1):
#             print(f" {i}. {b}")
#         print("" + "-"*40)


# test_llm.py
"""
Test harness for StyleSavvy LLM prompts.
Evaluates multiple prompt templates and parses the generated outputs into distinct tips.
"""

from models.llm import StyleSavvy

# Variant prompt templates with placeholders
# PROMPTS = {
#     "direct_instruction": (
#         "You are a professional fashion stylist. A client with a {body_type}-shaped body "
#         "and {face_shape} face is preparing for {occasion}. They are currently wearing: {items}. "
#         "Give exactly five distinct styling tips to improve their outfit. "
#         "Each tip should be concise, actionable, and start on a new line."
#     ),
#     "category_expansion": (
#         "As a high-end fashion advisor, provide five styling tips for a {body_type}-shaped person "
#         "with a {face_shape} face attending {occasion}. They are wearing {items}. "
#         "Offer one tip each for silhouette, color, accessories, footwear, and layering, "
#         "each on its own line."
#     ),
#     "event_aesthetic": (
#         "Imagine curating the perfect outfit for a {body_type}-shaped individual with a {face_shape} face "
#         "at {occasion}. They are wearing {items}. Suggest 5 ways to enhance their style, "
#         "focusing on event-appropriate aesthetics. Separate each tip with a newline."
#     ),
#     "fashion_editor": (
#         "As a fashion editor, outline five unique styling tips for a {body_type}-shaped reader with a {face_shape} face "
#         "attending {occasion}. They wear {items}. Each recommendation should reflect expertise and relevance. "
#         "List each tip on a new line."
#     ),
#     "influencer_style": (
#         "You’re an influencer giving sharp styling advice. A follower with a {body_type} body and {face_shape} face "
#         "is going to {occasion}, wearing {items}. Reply with five snappy, modern style tips, "
#         "each on its own line."
#     ),
# }

PROMPTS = {
    "direct_instruction": (
        "You are a world-renowned fashion stylist celebrated for your bold creativity and attention to detail. "
        "Your {gender} client has a {body_type}-shaped silhouette and a {face_shape} face, preparing for the {occasion}. "
        "They’re wearing {items}. In vivid, sensory-rich language, provide one transformative styling recommendation that considers the event’s ambiance, lighting, and dress code. "
        "Use dynamic adjectives and actionable insight to elevate their entire look."
    ),
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


# Test parameters
BODY_TYPE = "Slim"
FACE_SHAPE = "SQUARE"
OCCASION = "BEACH PARTY"
ITEMS = ["jeans", "jacket", "shoes",'shirt']
GENDER = "Male"

if __name__ == "__main__":
    advisor = StyleSavvy()

    for name, template in PROMPTS.items():
        print(f"=== Testing template: {name} ===")

        # Build prompt
        prompt = template.format(
            body_type=BODY_TYPE,
            face_shape=FACE_SHAPE,
            occasion=OCCASION,
            gender = GENDER,
            items=", ".join(ITEMS)

        )
        print("Prompt:\n" + prompt)

        # Generate response
        result = advisor.pipe(
            prompt,
            max_length=advisor.max_length,
            early_stopping=True,
            num_beams=4,
            no_repeat_ngram_size=3,  
            do_sample=False)[0]["generated_text"].strip()

        print("\nRaw generated output:\n" + result)

        # Parse into tips (bullets or sentence)
        lines = result.splitlines()
        tips = [ln.strip("-*0123456789. ").strip() for ln in lines if ln.strip()]
        if len(tips) < 3:
            # fallback to sentence split
            tips = [p.strip() for p in result.split(".") if p.strip()]
        tips = list(dict.fromkeys(tips))  # remove duplicates

        print(f"\n💡 Parsed {len(tips)} style tips:")
        for i, tip in enumerate(tips[:5], 1):
            print(f"{i}. {tip}")
        print("-" * 40)
