-- Top 10 Water Consuming Countries
SELECT
    f.country,
    ROUND(SUM(fm.daily_water_usage_gallons)::numeric, 2) AS total_water_usage
FROM facility_metrics fm
JOIN facilities f
ON fm.facility_id = f.facility_id
GROUP BY f.country
ORDER BY total_water_usage DESC
LIMIT 10;

-- Top 10 Electricity Consuming Countries
SELECT
    f.country,
    ROUND(SUM(fm.daily_electricity_usage_mwh)::numeric, 2) AS total_electricity
FROM facility_metrics fm
JOIN facilities f
ON fm.facility_id = f.facility_id
GROUP BY f.country
ORDER BY total_electricity DESC
LIMIT 10;

--Most Efficient Data Centers (Lowest PUE)
SELECT
    f.facility_name,
    ROUND(AVG(fm.pue)::numeric, 2) AS avg_pue
FROM facility_metrics fm
JOIN facilities f
ON fm.facility_id = f.facility_id
GROUP BY f.facility_name
ORDER BY avg_pue ASC
LIMIT 10;

--Water Stress Analysis
SELECT
    water_stress_tier,
    ROUND(AVG(daily_water_usage_gallons)::numeric, 2) AS avg_water_usage
FROM facility_metrics
GROUP BY water_stress_tier
ORDER BY avg_water_usage DESC;

--Yearly Electricity Trend
SELECT
    year,
    ROUND(SUM(daily_electricity_usage_mwh)::numeric, 2) AS total_usage
FROM facility_metrics
GROUP BY year
ORDER BY year;

