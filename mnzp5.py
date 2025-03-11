import pandas as pd
import matplotlib.pyplot as plt

url = "https://raw.githubusercontent.com/datasciencedojo/datasets/master/titanic.csv"
titanic = pd.read_csv(url)
print(titanic.head())
print(titanic.tail())
if 'Unnamed: 0' in titanic.columns:
    titanic.rename(columns={'Unnamed: 0': 'name'}, inplace=True)
if 'passengerClass' in titanic.columns:
    titanic.rename(columns={'passengerClass': 'class'}, inplace=True)
print("Наймолодший вік:", titanic['Age'].min())
print("Найстарший вік:", titanic['Age'].max())
print("Середній вік:", titanic['Age'].mean())
print("Медіана віку:", titanic['Age'].median())
survivors = titanic[titanic['Survived'] == 1]
print("Кількість виживших:", survivors.shape[0])
print("Середній вік виживших:", survivors['Age'].mean())
women_first = titanic[(titanic['Pclass'] == 1) & (titanic['Sex'] == 'female')]
women_first = women_first.sort_values('Age')
print(women_first[['Name', 'Age', 'Survived']])
print("Наймолодша жінка 1-го класу:", women_first['Age'].min())
print("Найстарша жінка 1-го класу:", women_first['Age'].max())
print("Кількість виживших жінок 1-го класу:", women_first[women_first['Survived'] == 1].shape[0])
plt.figure(figsize=(10,6))
plt.hist(titanic['Age'].dropna(), bins=30, edgecolor='black')
plt.title("Гістограма розподілу віку пасажирів")
plt.xlabel("Вік")
plt.ylabel("Частота")
plt.show()
