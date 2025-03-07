import seaborn as sns
import matplotlib.pyplot as plt
import pandas as pd
import numpy as np  

# Загрузка файла (замените 'laba11.csv' на имя вашего файла)
df = pd.read_csv('mnzp.csv')

# Общая информация о DataFrame: типы данных, количество непустых значений
print(df.info())
non_null_counts = df.notnull().sum().sort_values(ascending=False)
print(non_null_counts)