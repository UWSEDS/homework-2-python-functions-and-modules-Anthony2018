#this is test for the function.py
import numpy as np
import pandas as pd
#import matplotlib as plt
import requests
import function as fun

def save_file(url, file_name):
  r = requests.get(url)
  with open(file_name, 'wb') as f:
    f.write(r.content)

save_file('https://inventory.data.gov/dataset/cedbc0ee-d679-4ebf-8b00-502dc0de5738/resource/ef734bd0-0aff-4687-9b8a-fc69b937be63/download/userssharedsdfratebrthsyaw1819raceethncty20002012.csv',
          'data.csv')

df = pd.read_csv('data.csv') 
name = df.columns.values.tolist()
ans = fun.test_create_dataframe(df, name)
print(ans)