import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

print ("Pandas version: ", pd.__version__)
df = pd.read_csv("data/StudentsPerformance.csv")
# print(df.head())
# print(df.columns)
# print(df.dtypes)

#print("Students")

# Customization
sns.set_theme(style="whitegrid")

x_ = "math score"
y_ = "parental level of education"

"""
# --- Scatter ---
fig, ax = plt.subplots(figsize=(12, 6)) # Matplotlib
sns.scatterplot(data=df, x=x_, y=y_, ax=ax, color="green", marker="o")
ax.set_title("Math score vs parental level of education")
ax.set_xlabel("Math score")
ax.set_ylabel("Level of education")

# --- Bar ---
fig, ax = plt.subplots(figsize=(12, 6)) # Matplotlib
sns.barplot(data=df, x=x_, y=y_, ax=ax, color="orange")
ax.set_title("Math score vs parental level of education")
ax.set_xlabel("Math score")
ax.set_ylabel("Level of education")

# --- Line ---
fig, ax = plt.subplots(figsize=(12, 6)) # Matplotlib
sns.lineplot(data=df, x=x_, y=y_, color="red", ax=ax)
ax.set_title("Math score vs parental level of education")
ax.set_xlabel("Math score")
ax.set_ylabel("Level of education")
"""
_ALLOWED_KWARGS = {
    "scatter": {"color", "marker", "alpha", "size", "hue", "style"},
    "bar":     {"color", "alpha", "hue", "palette", "errorbar"},
    "line":    {"color", "alpha", "hue", "linewidth", "linestyle"},
    "box":     {"color", "hue", "palette", "width", "linewidth"},
    "violin":  {"color", "hue", "palette", "width", "linewidth", "inner"},
    "hist":    {"color", "hue", "bins", "alpha", "palette"},
}

def plot(df, x, y, kind="scatter", title="", xlabel="", ylabel="", figsize=(12, 6), **kwargs):
    plot_funcs = {
        "scatter": sns.scatterplot,
        "bar":     sns.barplot,
        "line":    sns.lineplot,
        "box":     sns.boxplot,
        "violin":  sns.violinplot,
        "hist":    sns.histplot,
    }

    if kind not in plot_funcs:
        raise ValueError(f"Unknown kind '{kind}'. Available: {list(plot_funcs)}")

    # Only alloud kwargs for sertain types
    allowed = _ALLOWED_KWARGS.get(kind, set())
    filtered_kwargs = {k: v for k, v in kwargs.items() if k in allowed}

    fig, ax = plt.subplots(figsize=figsize)
    plot_funcs[kind](data=df, x=x, y=y, ax=ax, **filtered_kwargs)

    ax.set_title(title)
    ax.set_xlabel(xlabel)
    ax.set_ylabel(ylabel)

    plt.tight_layout()
    #plt.show(fig)
    #plt.close(fig)

# Customization
title  = "Math score vs parental level of education"
xlabel = "Math score"
ylabel = "Level of education"

plot(df, x_, y_, kind="box", title=title, xlabel=xlabel, ylabel=ylabel, color="green", marker="o")
plot(df, x_, y_, kind="hist",    title=title, xlabel=xlabel, ylabel=ylabel, color="blue")
plot(df, x_, y_, kind="bar",     title=title, xlabel=xlabel, ylabel=ylabel, color="orange")
plot(df, x_, y_, kind="violin",    title=title, xlabel=xlabel, ylabel=ylabel, color="blue")    

plt.show()
plt.close("all") 
