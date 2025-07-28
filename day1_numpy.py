!pip install openpyxl

import pandas as pd
import os

file_name = 'Sample Data Set.xlsx'

if os.path.exists(file_name):
  print(f"File '{file_name}' exists.")

  df = pd.read_excel(file_name)
  if df is not None:
    print("\nDataFrame loaded successfully.")
    
#print(df.head()) #show 1st 5 row only
#print(df.info()) #show data type
#print(df.describe()) #show statistic

#selected_columns = df[['Idx', 'T1']] #select certain column
#print(selected_columns.head())

#temp_slice = df.loc[0:100, 'Idx':'T3'] #select certain row
#print("\nFirst 100 rows and temp columns:")
#print(temp_slice)

hot_points = df[df['T1'] > 25.0] #select certain column with certain value (filter)
#print(hot_points)

#T2_T1 = df[df['T2-T1'] < 1.5]
#print(T2_T1)  # show dulu
#print(T2_T1.describe())  # then count

hot_points.sort_values(by='T2-T1', ascending=False)
