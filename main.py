import json
import pandas as pd
import numpy as np

# Loading file

with open('C:\\Users\\Istkhar Mohmmad\\Desktop\\crescent assign\\new_json_copy.json') as data_file:
    data = json.load(data_file)
json.dumps(data)
df = pd.DataFrame.from_dict(pd.json_normalize(data), orient='columns')
conditions = [(df['data'] == '%%@%%')]
choices = ["True", "False"]

# Adding FLAG column

df["FLAG"] = np.select(conditions, choices)
print(df.T)
