import pandas as pd

# Load dataset
df = pd.read_csv(r"C:\Users\malva\Desktop\AI-DataCenter-Sustainability-Pipeline\data\data_center_hybrid.csv")

print("\n=== DATA QUALITY REPORT ===\n")

# Shape
print("Dataset Shape:")
print(df.shape)

# Missing values
print("\nMissing Values:")
print(df.isnull().sum())

# Duplicate rows
print("\nDuplicate Rows:")
print(df.duplicated().sum())

# Remove duplicates
df = df.drop_duplicates()

# Create new metric
df["Water_Electricity_Ratio"] = (
    df["Daily_Water_Usage_Gallons"] /
    df["Daily_Electricity_Usage_MWh"]
)

print("\nNew Column Added:")
print("Water_Electricity_Ratio")

# Save transformed data
df.to_csv(
    "data/processed_data.csv",
    index=False
)

print("\nProcessed file saved successfully!")
print("\nFinal Shape:")
print(df.shape)