import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

df = pd.read_csv('CigarettesSW.csv')
df_1985 = df[df['year'] == 1985].copy()
df_1985 = df_1985.sort_values('state')

print("Перші 5 рядків DataFrame:")
print(df_1985.head())
print("\nОстанні 5 рядків DataFrame:")
print(df_1985.tail())
print("\nІнформація про DataFrame:")
df_1985.info()


mean_price = df_1985['price'].mean()
print("\nСередня ціна сигарет:", mean_price)
df_high_price = df_1985[df_1985['price'] > mean_price]
print("\nРядки, де ціна сигарет вище за середню:")
print(df_high_price[['state', 'price']])


print("\nПерший рядок (за допомогою iloc):")
print(df_1985.iloc[0])


if 'CA' in df_1985['state'].values:
    print("\nДані для штату 'CA' (за допомогою loc):")
    print(df_1985.loc[df_1985['state'] == 'CA'])


state_idx = df_1985.columns.get_loc('state')
price_idx = df_1985.columns.get_loc('price')
subset = df_1985.iloc[2:6, [state_idx, price_idx]]
print("\nПідмножина даних (рядки 2-5, стовпці 'state' і 'price') за допомогою iloc:")
print(subset)


print("\nТранспонований DataFrame (перші 3 рядки):")
print(df_1985.head(3).T)


price_series = df_1985['price']
print("\nSeries з ціни сигарет:")
print(price_series)


print("\nСтатистичні характеристики Series 'price':")
print("Середнє:", price_series.mean())
print("Медіана:", price_series.median())
print("Мода:", price_series.mode().values)
print("Дисперсія (генеральної сукупності):", price_series.var(ddof=0))
print("Стандартне відхилення (генеральної сукупності):", price_series.std(ddof=0))




df_sorted_price = df_1985.sort_values(by='price', ascending=False)
print("\nDataFrame, відсортований за ціною сигарет (за спаданням):")
print(df_sorted_price[['state', 'price']].head())

df_grouped = df_1985.groupby('state')['price'].mean().reset_index()
print("\nСередня ціна сигарет для кожного штату:")
print(df_grouped)

df_1985_renamed = df_1985.rename(columns={'price': 'Price', 'tax': 'Tax'})
print("\nDataFrame з перейменованими стовпцями:")
print(df_1985_renamed.head())



plt.figure(figsize=(12, 6))
plt.plot(df_1985['state'], df_1985['price'], marker='o', label='Ціна сигарет')
plt.plot(df_1985['state'], df_1985['tax'], marker='o', label='Податок')
plt.title("Залежність ціни сигарет від податку за штатами (1985)")
plt.xlabel("Штат")
plt.ylabel("Значення")
plt.xticks(rotation=90)
plt.legend()
plt.tight_layout()
plt.show()
