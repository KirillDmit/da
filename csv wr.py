import pandas as pd

file = pd.read_csv('works.csv')

print(len(file))
print(len(file[file.gender == "Мужской"]))
print(len(file[file.gender == "Женский"]))
print(file.skills.dropna())
print(len(file[file.skills.notna()]))

my_series = pd.Series([5, 6, 7])

print(my_series)

file.groupby(['salary'])

print(file)

