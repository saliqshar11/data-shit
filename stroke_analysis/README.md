# Stroke Risk Factor Analysis

## Overview
Exploratory analysis of a stroke patient dataset sourced from Kaggle.
The goal was to identify the predominant factors associated with stroke risk.

## Dataset
- **Source:** Kaggle - Stroke Prediction Dataset
- **Size:** 5,110 patients, 12 variables
- **Key columns:** age, BMI, glucose level, hypertension, smoking status, stroke outcome

## Findings

### 1. Age is the dominant factor
Stroke cases were heavily concentrated in the elder population (60+).
All further analysis was scoped to this age group to control for age effects.

### 2. BMI produced a counterintuitive result
Expected obese patients to have the highest stroke rate.
Instead, normal weight elders had the highest stroke percentage —
higher than obese elders. This prompted further investigation.

### 3. Hypertension is linked to BMI but doesn't explain the anomaly
Hypertension rates scale linearly with BMI as expected.
However hypertension alone could not explain why normal weight elders
were at higher risk than obese elders.

### 4. Glucose level is the key driver
When controlling for glucose levels, the picture became clear.
Diabetic patients had the highest stroke rates regardless of BMI —
normal weight diabetic elders matched obese diabetic elders at 17%.

**Conclusion:** For the elder population, diabetic state is a stronger
stroke predictor than BMI. Normal weight individuals are not protected
from stroke risk if their glucose levels are in the diabetic range.

## Tools
- Python, pandas, SQLite, SQL