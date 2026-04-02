
## Project Structure

hearts/  
├── data/        # input datasets (CSV)  
├── scripts/     # all processing and model scripts  
├── outputs/     # logs and results  
├── .venv/       # virtual environment  
├── main.py      # CLI entry point


## Data Source

Dataset used in this project:

- [Heart Disease Dataset (Heart.csv)](https://github.com/rashida048/Datasets/blob/master/Heart.csv?utm_source=chatgpt.com)

**Description (short):**  
This dataset contains medical attributes of patients and a binary target indicating the presence of heart disease (`AHD`).  
It includes features such as age, sex, chest pain type, cholesterol level, maximum heart rate, and others commonly used for classification tasks.


# Installation

## 1. Clone repository

git clone <your-repo-url>  
cd hearts



## 2. Create virtual environment

python -m venv .venv

Activate:

**Windows (PowerShell / CMD):**

.venv\Scripts\activate

**Linux / Mac:**

source .venv/bin/activate



## 3. Install dependencies

pip install pandas scikit-learn matplotlib seaborn

eller: pip install req.txt

---

## 4. Add dataset

Download the dataset from:

- [Heart.csv download](https://github.com/rashida048/Datasets/blob/master/Heart.csv?utm_source=chatgpt.com)

Place it into:

data/heart.csv



#  How to Run

Start the CLI menu:

python main.py

-

#  Available Actions

=== DATA ===  
0. View raw data  

1. Clean data  
2. Visualize data  
3. Prepare data  

=== MODELS ===  
4. Logistic Regression (no scaling)  
5. Logistic Regression (scaled)  
6. k-NN (tuning)  
7. Decision Tree  
8. Random Forest  

=== APPLICATION ===  
9. Patient diagnosis



##  Notes

- Models are trained using processed data from `heart_prepared.csv`
- Best performing model in this project: **k-NN with scaling (k=11)**
- Diagnosis module uses trained pipeline to predict disease risk

> All input features were scaled using StandardScaler before training 
> the Logistic Regression and k-NN models.
> 
> Scaling was applied to the entire feature set, including both 
> numerical and one-hot encoded categorical variables.
---

## 📌 Short Summary

This project demonstrates a full ML pipeline:  
raw data → cleaning → visualization → modeling → diagnosis
