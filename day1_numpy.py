!pip install openpyxl

import pandas as pd
import os

file_name = 'Sample Data Set.xlsx'

if os.path.exists(file_name):
  print(f"File '{file_name}' exists.")

  df = pd.read_excel(file_name)
  if df is not None:
    print("\nDataFrame loaded successfully.")
    
