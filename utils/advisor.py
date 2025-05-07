from models.llm import StyleSavvy

advisor = StyleSavvy()

def get_advice(items, body_type, face_shape, gender,occasion):
    return advisor.advise(items, body_type, face_shape, gender, occasion)

