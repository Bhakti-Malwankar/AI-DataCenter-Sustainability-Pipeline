import pandas as pd

# Read dataset
df = pd.read_csv(r"C:\Users\malva\Desktop\AI-DataCenter-Sustainability-Pipeline\data\data_center_hybrid.csv")

print("\nDataset Loaded Successfully!\n")

print("Rows, Columns:")
print(df.shape)

print("\nColumns:")
print(df.columns.tolist())

print("\nFirst 5 Records:")
print(df.head())