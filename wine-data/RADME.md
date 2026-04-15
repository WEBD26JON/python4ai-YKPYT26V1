# 🍷 Wine Quality Classifier
**Python för AI-utveckling · YKPYT26V1**

A machine learning pipeline for wine quality classification
based on chemical composition.
Classifies wines as `ordinary` (quality 3–5) or `high` (quality 6–9).

---

## Documentation

| File | Description |
|------|-------------|
| [rapport.md](rapport.md) | Project report (Swedish) — full pipeline description, model results, bias analysis |
| [data-help.md](data-help.md) | Feature descriptions and chemical parameter reference |

---

## Project Structure
<pre>
wine-data/
├── data/
│   ├── wine-data-raw.csv        # raw dataset
│   ├── wine-clean.csv           # after cleaning
│   ├── wine-prepared-2.csv      # binary: ordinary / high
│   ├── wine-prepared-3a.csv     # 3 classes: low / medium / high
│   └── wine-prepared-3b.csv     # 3 classes: low / medium / high (alt)
├── outputs/
│   └── *.txt                    # logs and reports
├── tools/
│   ├── init.py
│   └── logger.py
├── scripts/
│   ├── data-preview.py          # raw data inspection
│   ├── data-clean.py            # cleaning and deduplication
│   ├── data-vis.py              # visualization (Matplotlib)
│   ├── data-prepare.py          # encoding, target creation
│   ├── dtree.py                 # Decision Tree
│   ├── knn.py                   # k-Nearest Neighbors
│   ├── rf.py                    # Random Forest
│   └── wine-test.py         # Gradio web application
├── main.py                      # CLI launcher
└── req.txt                      # dependencies
</pre>

---

## Data Source

[Wine Quality Dataset](https://github.com/bencmbit/datasets/blob/master/red-wine.csv)
· GitHub · bencmbit/datasets

6 497 samples · 11 chemical features · red and white wines
(Vinho Verde, Portugal)

---

## Installation

**1. Clone repository**
```bash
git clone https://github.com/Soviet9773Red/python4ai-YKPYT26V1
cd wine-data
```

**2. Create virtual environment**
```bash
python -m venv .venv
```

Activate:
```bash
# Windows
.venv\Scripts\activate

# Linux / Mac
source .venv/bin/activate
```

**3. Install dependencies**
```bash
pip install -r req.txt
```

---

## How to Run

**CLI launcher (data pipeline + models):**
```bash
python main.py
```

**Web application (Gradio):**
```bash
python scripts/wine-test.py
```
Opens automatically at `http://127.0.0.1:7860`

---

## Results

| Model          | Accuracy | Parameters  |
|----------------|----------|-------------|
| Random Forest  | **0.757**| depth=None  |
| Decision Tree  | 0.740    | depth=5     |
| k-NN           | 0.730    | k=7, k=11   |

Best model: **Random Forest (depth=None)** on binary classification.

---

## Notes

- Best model trained on `wine-prepared-2.csv` (binary target)
- Scaling with `StandardScaler` applied for k-NN only
- Gradio app uses Random Forest with `predict_proba` for confidence output
- Dataset limited to Vinho Verde region — results may not generalize
