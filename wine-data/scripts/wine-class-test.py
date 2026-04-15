import pandas as pd
df = pd.read_csv("data/wine-clean.csv")
bins = [2, 4, 6, 9]
labels = ["low", "medium", "high"]
df["quality_class"] = pd.cut(df["quality"], bins=bins, labels=labels)
print(df["quality_class"].value_counts().sort_index())
print()
print(df["quality"].value_counts().sort_index())