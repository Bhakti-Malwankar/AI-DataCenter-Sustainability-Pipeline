import pandas as pd
from sqlalchemy import create_engine

DATABASE_URL = (
    "postgresql+psycopg2://postgres:Bhakti5@localhost:5432/ai_datacenter_pipeline"
)

engine = create_engine(DATABASE_URL)

query = """
SELECT
    f.country,
    ROUND(SUM(fm.daily_water_usage_gallons)::numeric, 2) AS total_water_usage
FROM facility_metrics fm
JOIN facilities f
ON fm.facility_id = f.facility_id
GROUP BY f.country
ORDER BY total_water_usage DESC
LIMIT 10;
"""

result = pd.read_sql(query, engine)

print("\n=== TOP 10 WATER CONSUMING COUNTRIES ===\n")
print(result)