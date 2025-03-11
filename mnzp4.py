import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv("CigarettesSW.csv")
states_to_plot = ['CA', 'TX', 'NY']

plt.figure(figsize=(12, 6))
for state in states_to_plot:
    data = df[df['state'] == state].copy()
    data = data.sort_values('year')
    # Припускаємо, що "year" знаходиться на позиції 1, а "pop" (популяція) — на позиції 5
    x = data.iloc[:, 1]
    y = data.iloc[:, 5]
    plt.plot(x, y, marker='o', label=state)

plt.title("Популяція обраних штатів через роки")
plt.xlabel("Рік")
plt.ylabel("Популяція")
plt.legend()
plt.tight_layout()
plt.show()


