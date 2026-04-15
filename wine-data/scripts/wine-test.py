# wine-test.py
from pathlib import Path
import pandas as pd
import gradio as gr
import socket

from sklearn.ensemble import RandomForestClassifier
from sklearn.model_selection import train_test_split

# ── Train model ──────────────────────────────────────────────
BASE_DIR = Path(__file__).resolve().parent.parent
DATA_DIR = BASE_DIR / "data"

df = pd.read_csv(DATA_DIR / "wine-prepared-2.csv")

X = df.drop(columns=["quality_class"])
y = df["quality_class"]

X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.25, random_state=42, stratify=y
)

model = RandomForestClassifier(n_estimators=100, max_depth=None, random_state=42)
model.fit(X_train, y_train)

FEATURE_COLS = X.columns.tolist()

# ── Predict function ──────────────────────────────────────────
def predict(color, fixed_acidity, volatile_acidity, citric_acid,
            residual_sugar, chlorides, free_so2, total_so2,
            density, ph, sulphates, alcohol):

    color_val = 0 if color == "red" else 1

    input_data = pd.DataFrame([{
        "fixed acidity":        fixed_acidity,
        "volatile acidity":     volatile_acidity,
        "citric acid":          citric_acid,
        "residual sugar":       residual_sugar,
        "chlorides":            chlorides,
        "free sulfur dioxide":  free_so2,
        "total sulfur dioxide": total_so2,
        "density":              density,
        "pH":                   ph,
        "sulphates":            sulphates,
        "alcohol":              alcohol,
        "color":                color_val,
    }])

    input_data = input_data.reindex(columns=FEATURE_COLS)

    pred = model.predict(input_data)[0]
    proba = model.predict_proba(input_data)[0]
    classes = model.classes_
    proba_dict = dict(zip(classes, proba))
    p_high = proba_dict.get("high", 0)

    if p_high >= 0.65:
        verdict = "🏆 High quality"
        comment = "The chemical profile matches a high-quality wine."
    elif p_high >= 0.50:
        verdict = "🥈 Good quality"
        comment = "Above average. Likely a decent wine but not premium."
    elif p_high >= 0.35:
        verdict = "🥉 Borderline case"
        comment = "On the class boundary. Possible mismatch with declared quality."
    else:
        verdict = "🍶 Ordinary wine"
        comment = "Parameters do not correspond to a high quality class."

    result = (
        f"## {verdict}\n\n"
        f"**Probability:**&nbsp;  high ~ {p_high:.1%} &nbsp;|&nbsp; ordinary ~ {1 - p_high:.1%}  \n"
        f"_{comment}_"
    )

    return result, round(p_high * 100, 1)

# GRADIO PART

HELP_TEXT = (
    f"<div style='text-align:left; opacity:0.9; font-size:13px;'>"
    "Chemical parameters:\n\n"
    "- **fixed acidity** — fixed acids, contributes to wine structure\n"
    "- **volatile acidity** — acetic acid, high values give vinegar taste\n"
    "- **citric acid** — freshness and flavour\n"
    "- **residual sugar** — sugar remaining after fermentation\n"
    "- **chlorides** — salt content\n"
    "- **free sulfur dioxide** — active preservative (SO₂)\n"
    "- **total sulfur dioxide** — total SO₂ including bound form\n"
    "- **density** — related to sugar and alcohol content\n"
    "- **pH** — acidity level (lower = more acidic)\n"
    "- **sulphates** — antimicrobial additive\n"
    "- **alcohol** — alcohol content in percent\n\n"
    "**Quality classes:**\n\n"
    "- **ordinary** — quality 3–5\n"
    "- **high** — quality 6–9\n"
    "</div>"
)

DISCLIMER = (
    "> **Disclaimer**"
    f"<div style='opacity:0.7; font-size:11px;'>"
    " This model is trained on a limited dataset: "
    " 5 320 samples after cleaning.<br> Low-quality wines"
    " (quality 3–4) are significantly underrepresented"
    " (< 5% of data), which reduces the model's ability"
    " to reliably detect them.<br> Results should be treated"
    " as indicative, not conclusive.<br>"
    " Accuracy on test data: <b>0.757<b>"
    "</div>"
)

# ── Interface ─────────────────────────────────────────────────
with gr.Blocks(title="Wine Quality Classifier") as app:

    gr.Markdown("# 🍷 Wine Quality Classifier\nEnter the chemical parameters of the wine to assess its quality class.")

    with gr.Row():
        with gr.Column():
            gr.Markdown("### Key parameters")
            color       = gr.Radio(["red", "white"], label="Wine type (color)", value="red")
            alcohol     = gr.Slider(8.0, 15.0, value=10.5, step=0.1,  label="Alcohol (%)")
            volatile_ac = gr.Slider(0.08, 1.58, value=0.35, step=0.01, label="Volatile acidity")
            sulphates   = gr.Slider(0.22, 2.0,  value=0.53, step=0.01, label="Sulphates")

            btn = gr.Button("🔍 Classify wine", variant="primary", scale=0)
            output = gr.Markdown()
            confidence = gr.Slider(0, 100, label="Model confidence - HIGH (%)", interactive=False)

        with gr.Column():
            gr.Markdown("### Chemical composition")
            with gr.Row():
                fixed_ac    = gr.Number(value=7.2,    label="Fixed acidity  [3.8–15.9]")
                citric      = gr.Number(value=0.31,   label="Citric acid  [0.0–1.66]")
                sugar       = gr.Number(value=3.0,    label="Residual sugar  [0.6–30.0]")
                chlorides   = gr.Number(value=0.047,  label="Chlorides  [0.009–0.611]")
            with gr.Row():
                free_so2    = gr.Number(value=30.0,   label="Free sulfur dioxide  [1–72]")
                total_so2   = gr.Number(value=100.0,  label="Total sulfur dioxide  [6–440]")
                density     = gr.Number(value=0.9940, label="Density  [0.9871–1.0037]")
                ph          = gr.Number(value=3.21,   label="pH  [2.72–4.01]")

            gr.Markdown(HELP_TEXT)

    btn.click(
        fn=predict,
        inputs=[color, fixed_ac, volatile_ac, citric, sugar,
                chlorides, free_so2, total_so2, density, ph,
                sulphates, alcohol],
        outputs=[output, confidence]
    )

    gr.Markdown("---")
    gr.Markdown(DISCLIMER)

def get_local_ip():
    s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    try:
        s.connect(("8.8.8.8", 80))
        ip = s.getsockname()[0]
    finally:
        s.close()
    return ip

ip = get_local_ip()

if __name__ == "__main__":
    
    port = 7860
    print(f"GRADIO local server: http://127.0.0.1:{port}/?__theme=dark")
    print(f"LAN access:  http://{ip}:{port}/?__theme=dark")
    app.launch(
        server_name="0.0.0.0",
        server_port=port
    )
    print("GRADIO: server closed")