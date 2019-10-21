'''Create a python module (a file with extension ‘.py’) with the following functions:

(1 points) Write a python reads creates a dataframe from a URL that points to a CSV file such as the pronto data or CSVs in data.gov.

(6 points) Create the function test_create_dataframe that takes as input: (a) a pandas DataFrame and (b) a list of column names. The function returns True if the following conditions hold:

The DataFrame contains only the columns that you specified as the second argument.
The values in each column have the same python type
There are at least 10 rows in the DataFrame.'''
import numpy as np
import pandas as pd
import requests

def save_file(url, file_name):
  r = requests.get(url)
  with open(file_name, 'wb') as f:
    f.write(r.content)

save_file('https://inventory.data.gov/dataset/cedbc0ee-d679-4ebf-8b00-502dc0de5738/resource/ef734bd0-0aff-4687-9b8a-fc69b937be63/download/userssharedsdfratebrthsyaw1819raceethncty20002012.csv',
          'data.csv')
df = pd.read_csv('data.csv') 
    
def test_create_dataframe(dataframe, colomnname):
    if dataframe.shape[0] < 10:
        return False
    namels = dataframe.columns.values.tolist()
    if namels != colomnname:
        return False
    rember_class = {}
    for ls in colomnname:
        rember_class[ls]=type(dataframe[ls][0])
        #print(rember_class)
        for i in range(dataframe.shape[0]): 
            if type(dataframe[ls][i])!=rember_class[ls]:
                return False
    return True




