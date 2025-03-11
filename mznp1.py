import pandas as pd
import statistics as stat
import seaborn as sns
import matplotlib.pyplot as plt
import numpy as np

df = pd.read_csv("CigarettesSW.csv")

df = df.replace(r'^\s*$', np.nan, regex=True)            
df["price"] = pd.to_numeric(df["price"], errors="coerce") 
df.dropna(subset=["price"], inplace=True)                 

values = list(df["price"])

print(f"Середнє (mean): {stat.mean(values)}")
print(f"Медіана (median): {stat.median(values)}")
try:   
    print(f"Мода (mode): {stat.mode(values)}")
except stat.StatisticsError as e:
    print(f"Мода (mode): Помилка обчислення (імовірно, декілька мод): {e}")

print(f"Дисперсія (генеральної сукупності) [pvariance]: {stat.pvariance(values)}")
print(f"Стандартне відхилення (генеральної сукупності) [pstdev]: {stat.pstdev(values)}")

