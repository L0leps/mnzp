import pandas as pd


data = {'A': [10, 20, 30], 'B': [40, 50, 60]}
df = pd.DataFrame(data, index=['row1', 'row2', 'row3'])


print("Значення at:", df.at['row2', 'A'])  # 20


print("Значення iat:", df.iat[1, 0])  # 20
