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
        verdict = "✅ Высокое качество (high)"
        comment = "Химический профиль соответствует качественному вину."
    elif p_high >= 0.40:
        verdict = "⚠️ Граничный случай"
        comment = "Вино находится на границе классов. Возможно несоответствие заявленному классу."
    else:
        verdict = "❌ Обычное вино (ordinary)"
        comment = "Параметры не соответствуют высокому классу качества."

    result = (
        f"## {verdict}\n\n"
        f"**Вероятность high:** {p_high:.1%}  \n"
        f"**Вероятность ordinary:** {1 - p_high:.1%}  \n\n"
        f"_{comment}_"
    )

    return result

# ── Interface ─────────────────────────────────────────────────
with gr.Blocks(title="Wine Quality Classifier") as app:

    gr.Markdown("# 🍷 Wine Quality Classifier\nВведите химические параметры вина для оценки качества.")

    with gr.Row():
        with gr.Column():
            gr.Markdown("### Основные параметры")
            color       = gr.Radio(["red", "white"], label="Тип вина (color)", value="red")
            alcohol     = gr.Slider(8.0, 15.0, value=10.5, step=0.1,  label="Алкоголь (alcohol %)")
            volatile_ac = gr.Slider(0.08, 1.58, value=0.35, step=0.01, label="Летучая кислота (volatile acidity)")
            sulphates   = gr.Slider(0.22, 2.0,  value=0.53, step=0.01, label="Сульфаты (sulphates)")

            output = gr.Markdown()

        with gr.Column():
            gr.Markdown("### Химический состав")
            fixed_ac    = gr.Number(value=7.2,    label="Фиксированная кислотность (fixed acidity)  [3.8–15.9]")
            citric      = gr.Number(value=0.31,   label="Лимонная кислота (citric acid)  [0.0–1.66]")
            sugar       = gr.Number(value=3.0,    label="Остаточный сахар (residual sugar)  [0.6–30.0]")
            chlorides   = gr.Number(value=0.047,  label="Хлориды (chlorides)  [0.009–0.611]")
            free_so2    = gr.Number(value=30.0,   label="Свободный SO₂ (free sulfur dioxide)  [1–72]")
            total_so2   = gr.Number(value=100.0,  label="Общий SO₂ (total sulfur dioxide)  [6–440]")
            density     = gr.Number(value=0.9940, label="Плотность (density)  [0.9871–1.0037]")
            ph          = gr.Number(value=3.21,   label="pH  [2.72–4.01]")

    btn = gr.Button("🔍 Определить качество", variant="primary")
    #output = gr.Markdown()

    btn.click(
        fn=predict,
        inputs=[color, fixed_ac, volatile_ac, citric, sugar,
                chlorides, free_so2, total_so2, density, ph,
                sulphates, alcohol],
        outputs=output
    )

if __name__ == "__main__":
    port = 7863
    print(f"Local server: http://127.0.0.1:{port}/?__theme=dark")
    app.launch(
        server_port=port
    )