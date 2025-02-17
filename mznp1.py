import seaborn as sns
import matplotlib.pyplot as plt
import pandas as pd
import statistics as stats

# Загрузка файла (замените 'laba1.csv' на имя вашего файла, если нужно)
df = pd.read_csv('laba1.csv')

print(df.head())
print(df.info())
print(df.describe())

# Предполагаем, что столбец '2024-M08' хранит числовые значения
# Переведём его в числовой тип (если там есть строки) и удалим пропуски
filtered_data = pd.to_numeric(df['2024-M08'], errors='coerce').dropna()

# Расчёт основных статистических показателей
mean_value = stats.mean(filtered_data)
median_value = stats.median(filtered_data)
mode_value = stats.mode(filtered_data)

print(f"Mean: {mean_value}, Median: {median_value}, Mode: {mode_value}")

variance = stats.pvariance(filtered_data)  # Дисперсия
std_dev = stats.pstdev(filtered_data)      # Стандартное отклонение

print(f"Variance: {variance}, Standard deviation: {std_dev}")

# Построение гистограммы
sns.histplot(filtered_data, bins=20, kde=True)
plt.title('Гистограмма для столбца 2024-M08')
plt.show()
