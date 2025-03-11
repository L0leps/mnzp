import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

df = pd.read_csv("CigarettesSW_rounded.csv")
import matplotlib.pyplot as plt
import seaborn as sns

plt.figure(figsize=(12, 6))
sns.histplot(df['price'], bins=30, kde=True, edgecolor='black')
plt.title("Розподіл цін по штатах")
plt.xlabel("Ціна")
plt.ylabel("Частота")
plt.tight_layout()
plt.show()

