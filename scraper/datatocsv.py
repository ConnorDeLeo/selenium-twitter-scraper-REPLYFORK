import pandas as pd

data = [
    {'A': 1, 'B': "str1", 'C': 123},
    {'A': 2, 'B': "str2", 'C': 456},
    {'A': 3, 'B': "str3", 'C': 789},
]

print("saving data to csv file...")

dataframe = pd.DataFrame(data)
dataframe.to_csv('replies.csv', index=False)
print("data saved.")