## Project Structure

hearts/  
├── data/        # input datasets (CSV)  
├── scripts/     # all processing and model scripts  
├── outputs/     # logs and results  
├── .venv/       # virtual environment  
├── main.py      # CLI entry point


hearts/<br>
├─ data/<br>
│   ├── heart_raw.csv<br>
│   ├── heart_clean.csv<br>
│   └──heart_prepared.csv<br>
├─ outputs/<br>
│   └── bias_report_YYYY-MM-DD_hhmmss.txt<br>
├── tools/<br>
│   ├── __init__.py<br>
│   └── logger.py<br>
├─ main.py<br>
├── scripts/<br>
    └── hearts-*.py<br>


## Data Source

Dataset used in this project:

- [Heart Disease Dataset (Heart.csv)](https://github.com/rashida048/Datasets/blob/master/Heart.csv)

**Description (short):**  
This dataset contains medical attributes of patients and a binary target indicating the presence of heart disease (`AHD`).  
It includes features such as age, sex, chest pain type, cholesterol level, maximum heart rate, and others commonly used for classification tasks.

# Installation

## 1. Clone repository

git clone <your-repo-url>  
cd hearts

## 2. Create virtual environment

`python -m venv .venv`

Activate:

**Windows (PowerShell / CMD):**

`.venv\Scripts\activate`

**Linux / Mac:**

`source .venv/bin/activate`

## 3. Install dependencies

`pip install pandas scikit-learn matplotlib seaborn`

or: `pip install req.txt`

---

## 4. Add dataset

Download the dataset from:

- [Heart.csv download](https://github.com/rashida048/Datasets/blob/master/Heart.csv)

Place it into:

data/heart.csv

## How to Run

Start the CLI menu:

`python main.py`

-

# Available Actions

HEART PROJECT<br>
 === DATA ===<br>
0. View raw data - hearts.csv<br>
1. Clean .csv data<br>
2. Visualize cleaned data<br>
3. Prepare data for models<br>

 === Models and tuning. ===<br>
4.  Logistic Regression: no scaling<br>
5.  Logistic Regression: scaled<br>
6.  k-NN model with different k<br>
7.  Decision Tree<br>
8.  Random Forest<br>
9.  Bias analys

 === APPLICATION ===<br>
D. Patient's diagnostic.

 === SYSTEM ===<br>
m Menu | e exit<br>

## Notes

- Models are trained using processed data from `heart_prepared.csv`
- Best performing model in this project: **k-NN with scaling (k=11)**
- Diagnosis module uses trained pipeline to predict disease risk

> All input features were scaled using StandardScaler before training 
> the Logistic Regression and k-NN models.
> 
> Scaling was applied to the entire feature set, including both 
> numerical and one-hot encoded categorical variables.

---

## Short Summary

This project demonstrates a full ML pipeline:  
raw data → cleaning → visualization → modeling → diagnosis<br>
Project rapport (swedish) : https://github.com/Soviet9773Red/python4ai-YKPYT26V1/blob/main/hearts/rapport.md
