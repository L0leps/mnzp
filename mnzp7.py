import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

df = pd.read_csv("CigarettesSW.csv")
corr_matrix = df.corr(numeric_only=True)
plt.figure(figsize=(8, 6))
sns.heatmap(corr_matrix, annot=True, cmap="coolwarm")
plt.title("Кореляційна матриця")
plt.tight_layout()
plt.show()
