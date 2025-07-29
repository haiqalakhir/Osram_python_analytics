import pandas as pd

# Load CSV
file_path = "CapstoneProject.csv"  # Change if Colab path is different
df = pd.read_csv(file_path)

df.isna().sum() #check null cells

clean_data = df.fillna(0)
print(clean_data.isna().sum())
