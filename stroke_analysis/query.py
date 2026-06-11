import sqlite3
import pandas as pd

conn = sqlite3.connect('stroke.db')

## Stroke percentage grouped by average BMI and Age Bracket
## Interesting thing to bserve is that normal weight elders have the highest percentage
## It is even higher than that of obese elders
query_bmi = """
SELECT
    CASE 
        WHEN bmi < 18.5 THEN 'Underweight'
        WHEN bmi < 25.0 THEN 'Normal'
        WHEN bmi < 30.0 THEN 'Overweight'
        ELSE 'Obese'
    END as bmi_category,
    CASE
        WHEN age < 20 THEN 'Teen'
        WHEN age >= 20 AND age < 40 THEN 'Early_Adulthood'
        WHEN age >= 40 AND age < 60 THEN 'Middle_Aged'
        ELSE 'Elder'
    END as age_bracket,
    COUNT(*) as total_patients,
    ROUND(100.0 * SUM(stroke) / COUNT(*), 2) as stroke_pct
FROM patients
GROUP BY bmi_category, age_bracket
ORDER BY stroke_pct DESC;
"""
## Hypothesis - Besides age the second most dominant factor is hypertension
## Problem - Hypertension is linked to obesety
## Solution query:
## Hypertension is indeed linked to weight
query_hypertension = """
SELECT
    CASE 
        WHEN bmi < 18.5 THEN 'Underweight'
        WHEN bmi < 25.0 THEN 'Normal'
        WHEN bmi < 30.0 THEN 'Overweight'
        ELSE 'Obese'
    END as bmi_category,
    ROUND(100.0 * SUM(hypertension) / COUNT(*), 2)as total_hypertension_patients
FROM patients
GROUP BY bmi_category
ORDER BY total_hypertension_patients DESC
"""

query_bmi_hypertension = """
SELECT
    CASE 
        WHEN bmi < 18.5 THEN 'Underweight'
        WHEN bmi < 25.0 THEN 'Normal'
        WHEN bmi < 30.0 THEN 'Overweight'
        ELSE 'Obese'
    END as bmi_category,
    ROUND(100.0 * SUM(hypertension) / COUNT(*), 2) as hypertension_pct,
    ROUND(100.0 * SUM(stroke) / COUNT(*), 2) as stroke_pct
FROM patients where age > 60
GROUP BY bmi_category
ORDER BY stroke_pct DESC
"""

## Acording to this last test:
## The main factor that causes stroke in elder population is glucose level
## The highest percentage of people who suffered from a stroke are:
## Diabetics with normal bmi.
query_gluc = """
SELECT 
    CASE
        WHEN avg_glucose_level < 100 THEN 'Normal'
        WHEN avg_glucose_level >= 100 AND avg_glucose_level < 125 THEN 'Prediabetic'
        ELSE 'Diabetic'
    END as diabetic_state,
    CASE 
        WHEN bmi < 18.5 THEN 'Underweight'
        WHEN bmi < 25.0 THEN 'Normal'
        WHEN bmi < 30.0 THEN 'Overweight'
        ELSE 'Obese'
    END as bmi_category,
    CASE
        WHEN age < 20 THEN 'Teen'
        WHEN age >= 20 AND age < 40 THEN 'Early_Adulthood'
        WHEN age >= 40 AND age < 60 THEN 'Middle_Aged'
        ELSE 'Elder'
    END as age_bracket,
    ROUND(100 * SUM(stroke) / COUNT(*), 2) as stroke_pct
FROM patients WHERE age > 60
GROUP BY diabetic_state, bmi_category, age_bracket
ORDER BY stroke_pct DESC;
"""
result_gluc = pd.read_sql(query_gluc,conn)
result_bmi_hypertension = pd.read_sql_query(query_bmi_hypertension, conn)
result_hypertension = pd.read_sql_query(query_hypertension, conn)
result_bmi = pd.read_sql_query(query_bmi, conn)

conn.close()