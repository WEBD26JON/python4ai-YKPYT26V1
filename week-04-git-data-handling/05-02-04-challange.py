import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

print ("Pandas version: ", pd.__version__)
df = pd.read_csv("data/delivery_times.csv")
# print(df.head())
# print(df.columns)
# print(df.dtypes)

print("There is a positive relationship: longer distance -> longer delivery time.")

# Customization
sns.set_theme(style="whitegrid")

x_ = "distance_km"
y_ = "delivery_minutes"

# --- Scatter ---
fig, ax = plt.subplots(figsize=(12, 6)) # Matplotlib
sns.scatterplot(data=df, x=x_, y=y_, ax=ax, color="green", marker="o")
ax.set_title("Delivery time in minutes vs distance")
ax.set_xlabel("Distance")
ax.set_ylabel("Minutes")

# --- Bar ---
fig, ax = plt.subplots() # Matplotlib
sns.barplot(data=df, x=x_, y=y_, ax=ax, color="orange")
ax.set_title("Delivery time in minutes vs distance")
ax.set_xlabel("Distance")
ax.set_ylabel("Minutes")

# --- Line ---
fig, ax = plt.subplots(figsize=(5, 7)) # Matplotlib
sns.lineplot(data=df, x=x_, y=y_, color="red", ax=ax)
ax.set_title("Delivery time in minutes vs distance")
ax.set_xlabel("Distance")
ax.set_ylabel("Minutes")

plt.show()
plt.close(fig)
