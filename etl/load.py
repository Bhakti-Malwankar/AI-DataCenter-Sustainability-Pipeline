import pandas as pd
from dotenv import load_dotenv
import os
from sqlalchemy import create_engine

load_dotenv()

DATABASE_URL = (
    f"postgresql+psycopg2://{os.getenv('DB_USER')}:"
    f"{os.getenv('DB_PASSWORD')}@"
    f"{os.getenv('DB_HOST')}:"
    f"{os.getenv('DB_PORT')}/"
    f"{os.getenv('DB_NAME')}"
)

engine = create_engine(DATABASE_URL)

# Load processed data
df = pd.read_csv("data/processed_data.csv")

# Create metrics dataframe
metrics_df = pd.DataFrame({
    "year": df["Year"],
    "facility_id": df["Facility_ID"],
    "estimated_capacity_mw": df["Estimated_Capacity_MW"],
    "pue": df["PUE"],
    "cooling_system_type": df["Cooling_System_Type"],
    "wue_l_per_kwh": df["WUE_L_per_kWh"],
    "daily_electricity_usage_mwh": df["Daily_Electricity_Usage_MWh"],
    "daily_water_usage_gallons": df["Daily_Water_Usage_Gallons"],
    "water_stress_tier": df["Surrounding_Water_Stress_Tier"],
    "water_electricity_ratio": df["Water_Electricity_Ratio"]
})

metrics_df.to_sql(
    "facility_metrics",
    engine,
    if_exists="append",
    index=False,
    chunksize=5000
)

print("✅ Facility Metrics Loaded Successfully!")
print(f"Rows inserted: {len(metrics_df)}")