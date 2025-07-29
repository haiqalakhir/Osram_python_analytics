import pandas as pd

# Load CSV
file_path = "CapstoneProject.csv"  # Change if Colab path is different
df = pd.read_csv(file_path)

df.isna().sum() #check null cells

clean_data = df.fillna(0)
print(clean_data.isna().sum())

numeric_t1 = df['T1'].apply(pd.to_numeric, errors='coerce')
clean_data = df.copy()
clean_data['T1'] = numeric_t1.fillna(numeric_t1.mean())
print(clean_data['T1'].isna().sum())

df.columns = df.columns.str.strip()
#df.duplicated().sum()
duplicated_data = df[df.duplicated()].sort_values(by='Idx')
#print(duplicated_data)
#duplicated_data.describe()
df['T1'] = df['T1'].replace('-', pd.NA)             #replace '-' to NA
df['T1'] = pd.to_numeric(df['T1'], errors='coerce') #convert to numeric
df.fillna(0, inplace=True)                          #fill NA into 0
df['T1'] = df['T1'].astype(float)                   #convert t1 into float

df_unique = df.drop_duplicates()                    #create a new dataframe with duplicate rows removed

df.drop_duplicates(inplace=True)

from scipy.stats import zscore
import matplotlib.pyplot as plt

df = df[df['T1'] != 0].copy()
df.loc[:, 'T1_zscore'] = zscore(df['T1'])

df.loc[:, 'zscore_outlier'] = df['T1_zscore'].apply(lambda x: 1 if abs(x) > 3 else 0)

plt.figure(figsize=(12, 6))
plt.plot(df.index, df['T1'], label='Raw T1', alpha=0.7)
outliers = df[df['zscore_outlier'] == 1]
plt.scatter(outliers.index, outliers['T1'], color='red', label='Z-score Outlier', zorder=5)
plt.title('T1 with Z-score Outliers')
plt.xlabel('Time')
plt.ylabel('Temp_delta (°C)')
plt.legend()
plt.grid(True)
plt.show()

df = df[df['T2'] != 0].copy()
df.loc[:, 'T2_zscore'] = zscore(df['T2'])

df.loc[:, 'zscore_outlier'] = df['T2_zscore'].apply(lambda x: 1 if abs(x) > 3 else 0)

plt.figure(figsize=(12, 6))
plt.plot(df.index, df['T2'], label='Raw T2', alpha=0.7)
outliers = df[df['zscore_outlier'] == 1]
plt.scatter(outliers.index, outliers['T2'], color='red', label='Z-score Outlier', zorder=5)
plt.title('T2 with Z-score Outliers')
plt.xlabel('Time')
plt.ylabel('Temp_delta (°C)')
plt.legend()
plt.grid(True)
plt.show()

df = df[df['T3'] != 0].copy()
df.loc[:, 'T3_zscore'] = zscore(df['T3'])

df.loc[:, 'zscore_outlier'] = df['T3_zscore'].apply(lambda x: 1 if abs(x) > 3 else 0)

plt.figure(figsize=(12, 6))
plt.plot(df.index, df['T3'], label='Raw T3', alpha=0.7)
outliers = df[df['zscore_outlier'] == 1]
plt.scatter(outliers.index, outliers['T3'], color='red', label='Z-score Outlier', zorder=5)
plt.title('T3 with Z-score Outliers')
plt.xlabel('Time')
plt.ylabel('Temp_delta (°C)')
plt.legend()
plt.grid(True)
plt.show()

from sklearn.ensemble import IsolationForest     # Select the features for anomaly detection
import matplotlib.pyplot as plt

features = df[['T1', 'T2', 'T3']]                # Initialize the model (random_state for reproducibility)
 
model = IsolationForest(random_state=42, contamination=0.01)         # Fit the model to our data (the model learns 'normal' patterns)
model.fit(features)                              # Predict anomalies: -1 for outlier, 1 for normal

df['anomaly_label_IF'] = model.predict(features) # Get a decision score (lower score = more anomalous)

num_anomalies = (df['anomaly_label_IF'] == -1).sum()
print(f"Number of anomalies: {num_anomalies}")

plt.figure(figsize=(12, 6))
plt.plot(df.index, df['T1'], label='Raw T1', alpha=0.7)
anomalies = df[df['anomaly_label_IF'] == -1]
plt.scatter(anomalies.index, anomalies['T1'], color='red', label='AI Anomalies', zorder=5)
plt.title('T1 with isolation forest anomalies')
plt.xlabel('Time')
plt.ylabel('Temperature (°C)')
plt.legend()
plt.grid(True)
plt.show()

plt.figure(figsize=(12, 6))
plt.plot(df.index, df['T2'], label='Raw T2', alpha=0.7)
anomalies = df[df['anomaly_label_IF'] == -1]
plt.scatter(anomalies.index, anomalies['T2'], color='red', label='AI Anomalies', zorder=5)
plt.title('T2 with isolation forest anomalies')
plt.xlabel('Time')
plt.ylabel('Temperature (°C)')
plt.legend()
plt.grid(True)
plt.show()

plt.figure(figsize=(12, 6))
plt.plot(df.index, df['T3'], label='Raw T3', alpha=0.7)
anomalies = df[df['anomaly_label_IF'] == -1]
plt.scatter(anomalies.index, anomalies['T3'], color='red', label='AI Anomalies', zorder=5)
plt.title('T1 with isolation forest anomalies')
plt.xlabel('Time')
plt.ylabel('Temperature (°C)')
plt.legend()
plt.grid(True)
plt.show()

df.to_excel('my_osram_analysis.xlsx', index=True)
print('report siap to my_osram_analysis')
