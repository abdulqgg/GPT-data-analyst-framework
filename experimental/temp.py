import pandas as pd
import numpy as np

df = pd.read_csv('Delivery truck trip data.csv')

# Convert trip durations to numerical values (assuming it's in minutes)
df['trip_duration'] = pd.to_numeric(df['actual_eta']) - pd.to_numeric(df['Planned_ETA'])

# Calculate Z-scores for trip durations
df['trip_duration_zscore'] = np.abs((df['trip_duration'] - df['trip_duration'].mean()) / df['trip_duration'].std())

# Define a threshold for outliers based on Z-score
threshold = 3
outliers = df[df['trip_duration_zscore'] > threshold]

print(outliers)