import gradio as gr
from utils.detector import detect_clothing
from utils.advisor  import get_advice

def run_style_savvy(image, bg_remove, body_type, face_shape, gender, occasion):
    # 1) Detect garments
    items = detect_clothing(image, do_bg_remove=bg_remove)
    # 2) Get raw advice string
    advice_list = get_advice(items, body_type, face_shape, gender, occasion)

    # 3) Filter duplicates, preserving order
    unique_advice = []
    seen = set()
    for tip in advice_list:
        if tip not in seen:
            unique_advice.append(tip)
            seen.add(tip)


    # 4) Build dark-themed HTML
    html = """
    <div style="
        background-color: #1e1e1e;
        color: #eeeeee;
        padding: 24px;
        border-radius: 12px;
        max-width: 600px;
        margin: auto;
    ">
      <h2 style="
          margin-top: 0;
          font-size: 2em;
          color: #ffa726;
          text-align: center;
      ">
        ✨ Your 5 Custom Style Tips ✨
      </h2>
      <ul style="
          list-style: disc inside;
          font-size: 1.2em;
          line-height: 1.6;
      ">
    """
    for advice in unique_advice:
        html += f"<li>{advice}</li>"
    html += "</ul></div>"

    return html

iface = gr.Interface(
    fn=run_style_savvy,
    inputs=[
        gr.Image(type="pil", label="Your Photo"),
        gr.Checkbox(label="Remove Background"),
        gr.Radio(["Slim","Athletic","Curvy","Plus-size"], label="Body Type"),
        gr.Radio(["Oval","Round","Square","Heart"],     label="Face Shape"),
        gr.Radio(["Male","Female"],     label="Gender"),
        gr.Textbox(label="Occasion"),
    ],
    outputs=gr.HTML(),  # render our styled HTML
    title="StyleSavvy",
    description="AI-powered fashion consultant. Upload your photo and get personalized style tips!",
)

if __name__ == "__main__":
    iface.launch()
