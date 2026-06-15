import os
import pandas as pd
from sqlalchemy import create_engine

# ==================================================
# DATABASE CONNECTION
# ==================================================

from dotenv import load_dotenv
import os


load_dotenv()

DATABASE_URL = (
    f"postgresql+psycopg2://{os.getenv('DB_USER')}:"
    f"{os.getenv('DB_PASSWORD')}@"
    f"{os.getenv('DB_HOST')}:"
    f"{os.getenv('DB_PORT')}/"
    f"{os.getenv('DB_NAME')}"
)

engine = create_engine(DATABASE_URL)

# ==================================================
# CREATE OUTPUT DIRECTORY
# ==================================================

os.makedirs("reports/output", exist_ok=True)

# ==================================================
# REPORT QUERIES
# ==================================================

queries = {

    "TOP_10_WATER_CONSUMING_COUNTRIES": """
        SELECT
            f.country,
            ROUND(SUM(fm.daily_water_usage_gallons)::numeric, 2) AS total_water_usage
        FROM facility_metrics fm
        JOIN facilities f
        ON fm.facility_id = f.facility_id
        GROUP BY f.country
        ORDER BY total_water_usage DESC
        LIMIT 10;
    """,

    "TOP_10_ELECTRICITY_CONSUMING_COUNTRIES": """
        SELECT
            f.country,
            ROUND(SUM(fm.daily_electricity_usage_mwh)::numeric, 2) AS total_electricity_usage
        FROM facility_metrics fm
        JOIN facilities f
        ON fm.facility_id = f.facility_id
        GROUP BY f.country
        ORDER BY total_electricity_usage DESC
        LIMIT 10;
    """,

    "TOP_COMPANIES_BY_WATER_CONSUMPTION": """
        SELECT
            f.owner_company,
            ROUND(SUM(fm.daily_water_usage_gallons)::numeric, 2) AS total_water
        FROM facility_metrics fm
        JOIN facilities f
        ON fm.facility_id = f.facility_id
        GROUP BY f.owner_company
        ORDER BY total_water DESC
        LIMIT 10;
    """,

    "WATER_STRESS_ANALYSIS": """
        SELECT
            water_stress_tier,
            ROUND(AVG(daily_water_usage_gallons)::numeric, 2) AS avg_water_usage
        FROM facility_metrics
        GROUP BY water_stress_tier
        ORDER BY avg_water_usage DESC;
    """,

    "COOLING_SYSTEM_EFFICIENCY": """
        SELECT
            cooling_system_type,
            ROUND(AVG(pue)::numeric, 2) AS avg_pue,
            ROUND(AVG(wue_l_per_kwh)::numeric, 2) AS avg_wue
        FROM facility_metrics
        GROUP BY cooling_system_type
        ORDER BY avg_pue ASC;
    """,

    "YEARLY_ELECTRICITY_CONSUMPTION_TREND": """
        SELECT
            year,
            ROUND(SUM(daily_electricity_usage_mwh)::numeric, 2) AS total_usage
        FROM facility_metrics
        GROUP BY year
        ORDER BY year;
    """,

    "YEAR_OVER_YEAR_ELECTRICITY_GROWTH": """
        SELECT
            year,
            ROUND(SUM(daily_electricity_usage_mwh)::numeric, 2) AS yearly_usage,

            ROUND(
                (
                    SUM(daily_electricity_usage_mwh)
                    -
                    LAG(
                        SUM(daily_electricity_usage_mwh)
                    ) OVER (ORDER BY year)
                )::numeric,
                2
            ) AS yearly_growth

        FROM facility_metrics
        GROUP BY year
        ORDER BY year;
    """
}

# ==================================================
# GENERATE REPORTS
# ==================================================

print("\n")
print("=" * 100)
print("AI DATA CENTER SUSTAINABILITY ANALYTICS REPORT")
print("=" * 100)

for report_name, query in queries.items():

    print(f"\n\n{report_name}")
    print("-" * 100)

    try:

        result = pd.read_sql(query, engine)

        # Display report
        print(result.to_string(index=False))

        # Save report to CSV
        output_file = f"reports/output/{report_name.lower()}.csv"

        result.to_csv(
            output_file,
            index=False
        )

        print(f"\n Saved: {output_file}")

    except Exception as e:

        print(f"\nError generating report:")
        print(e)

print("\n")
print("=" * 100)
print("REPORT GENERATION COMPLETED")
print("=" * 100)