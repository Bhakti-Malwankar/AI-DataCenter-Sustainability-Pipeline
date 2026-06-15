CREATE TABLE facilities (
    facility_id VARCHAR(50) PRIMARY KEY,
    facility_name VARCHAR(255),
    owner_company VARCHAR(255),
    city VARCHAR(100),
    country VARCHAR(100),
    facility_type VARCHAR(100)
);

CREATE TABLE facility_metrics (
    metric_id SERIAL PRIMARY KEY,
    year INT,
    facility_id VARCHAR(50),
    estimated_capacity_mw NUMERIC,
    pue NUMERIC,
    cooling_system_type VARCHAR(100),
    wue_l_per_kwh NUMERIC,
    daily_electricity_usage_mwh NUMERIC,
    daily_water_usage_gallons NUMERIC,
    water_stress_tier VARCHAR(50),
    water_electricity_ratio NUMERIC,

    FOREIGN KEY (facility_id)
    REFERENCES facilities(facility_id)
);