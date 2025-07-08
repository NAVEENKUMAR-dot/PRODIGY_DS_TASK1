# Import libraries
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Load the dataset (replace 'titanic.csv' with the correct path if needed)
df = pd.read_csv(r"C:\Users\kvnav\Downloads\titanic\train.csv")

# Set seaborn style
sns.set(style="whitegrid")

# -----------------------------
# 1. Bar Chart: Gender Distribution
# -----------------------------
plt.figure(figsize=(6, 4))
sns.countplot(data=df, x='Sex', palette='pastel')
plt.title('Gender Distribution of Titanic Passengers')
plt.xlabel('Gender')
plt.ylabel('Count')
plt.tight_layout()
plt.show()

# -----------------------------
# 2. Histogram: Age Distribution
# -----------------------------
plt.figure(figsize=(8, 5))
sns.histplot(data=df, x='Age', bins=30, kde=True, color='skyblue')
plt.title('Age Distribution of Titanic Passengers')
plt.xlabel('Age')
plt.ylabel('Frequency')
plt.tight_layout()
plt.show()
