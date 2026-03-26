from pathlib import Path

import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
# Create the Dataset
# week5/
#   data/
#     study_performance.csv
#   tasks/
#     linear_regression_demo.py

# Example B: Load Data and Define Feature and Target
BASE_DIR = Path(__file__).resolve().parent.parent
DATA_DIR = BASE_DIR / "data"

df = pd.read_csv(DATA_DIR / "study_performance.csv")

print(df.head())
print(df.columns)

feature_column = "hours_studied"
target_column = "test_score"

X = df[[feature_column]]
y = df[target_column]

print(type(X))
print(type(y))

# Example C: Split into Training and Test Data
X_train, X_test, y_train, y_test = train_test_split(
    X,
    y,
    test_size=0.25,
    random_state=42
)

# Example D: Create and Fit the Model
model = LinearRegression()
model.fit(X_train, y_train)

# Example E: Make Predictions
predictions = model.predict(X_test)

results_df = X_test.copy()
results_df["actual_score"] = y_test.values
results_df["predicted_score"] = predictions

print("Comparison table:")
print(results_df)

print("Predicted values:")
print(predictions)

print("Actual values:")
print(y_test.values)

# Example F: Predict a New Value
new_data = pd.DataFrame({feature_column: [9]})
new_prediction = model.predict(new_data)
print(f"Predicted score for 9 study hours: {new_prediction[0]:.2f}")