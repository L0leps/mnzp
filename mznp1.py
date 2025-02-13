import seaborn as sns
import matplotlib.pyplot as plt
import pandas as pd
import statistics as stats

# Завантаження файлу (замінити 'file.csv' на назву твого файлу)
df = pd.read_csv('laba1.csv')

print(df.head())

print(df.info())
print(df.describe())


mean_value = stats.mean(df['Базисний період'])
median_value = stats.median(df['Базисний період'])
mode_value = stats.mode(df['Базисний період'])

print(f"Mean: {mean_value}, Median: {median_value}, Mode: {mode_value}")
variance = stats.pvariance(df['Базисний період'])  # Дисперсія
std_dev = stats.pstdev(df['Базисний період'])      # Стандартне відхилення

print(f"Variance: {variance}, Standard deviation: {std_dev}")
import matplotlib.pyplot as plt
import seaborn as sns

sns.histplot(df[' Базисний період'], bins=20, kde=True)
plt.title('Гістограма для вибраних даних')
plt.show()
