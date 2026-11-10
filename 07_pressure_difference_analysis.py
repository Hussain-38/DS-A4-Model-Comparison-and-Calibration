# -*- coding: utf-8 -*-
"""
Created on Mon Nov  9 17:01:31 2026

@author: hussa
"""


# ============================================================
# DS-A4: MODEL COMPARISON AND CALIBRATION LAB
# STEP 7: PRESSURE DIFFERENCE ANALYSIS
# ============================================================

import pandas as pd
import numpy as np
from pathlib import Path

# ------------------------------------------------------------
# 1. LOAD DATASET
# ------------------------------------------------------------

PROJECT_DIR = Path(
    r"D:\Data Science Assignment\My Projects\DS-A4"
)

DATA_PATH = PROJECT_DIR / "raw dataset" / "S3.xls"

OUTPUT_DIR = PROJECT_DIR / "results" / "tables"
OUTPUT_DIR.mkdir(parents=True, exist_ok=True)

df = pd.read_excel(
    DATA_PATH,
    sheet_name=0,
    header=1,
    engine="xlrd"
)

df = df.dropna(axis=1, how="all")

df.columns = [
    "Source", "Rock", "Sample", "Al2SiO5", "Opaque",
    "T_GB00_GASP", "P_GASP", "T_GB00_GBPQ",
    "P_GBPQ_Mg", "P_GBPQ_Fe",
    "Fe_Bt", "Mg_Bt", "AlVI_Bt", "Ti_Bt",
    "Ca_Pl", "Na_Pl", "K_Pl",
    "Fe_Grt", "Mg_Grt", "Ca_Grt", "Mn_Grt"
]

# ------------------------------------------------------------
# 2. CALCULATE PRESSURE DIFFERENCES
# ------------------------------------------------------------

df["Difference_Mg"] = (
    df["P_GBPQ_Mg"] - df["P_GASP"]
)

df["Difference_Fe"] = (
    df["P_GBPQ_Fe"] - df["P_GASP"]
)

# Absolute differences

df["Absolute_Difference_Mg"] = (
    df["Difference_Mg"].abs()
)

df["Absolute_Difference_Fe"] = (
    df["Difference_Fe"].abs()
)

# ------------------------------------------------------------
# 3. DEFINE SUMMARY FUNCTION
# ------------------------------------------------------------

def calculate_metrics(difference):

    return {
        "Mean_Bias": difference.mean(),

        "MAE": difference.abs().mean(),

        "RMSE": np.sqrt(
            np.mean(difference ** 2)
        ),

        "Median_Difference": difference.median(),

        "Standard_Deviation": difference.std(),

        "Minimum_Difference": difference.min(),

        "Maximum_Difference": difference.max()
    }

# ------------------------------------------------------------
# 4. CALCULATE COMPARISON METRICS
# ------------------------------------------------------------

results = pd.DataFrame({
    "GBPQ_Mg": calculate_metrics(
        df["Difference_Mg"]
    ),

    "GBPQ_Fe": calculate_metrics(
        df["Difference_Fe"]
    )
})

print("\n========== PRESSURE COMPARISON ==========")

print(results.round(4))

# ------------------------------------------------------------
# 5. COUNT POSITIVE AND NEGATIVE DIFFERENCES
# ------------------------------------------------------------

print("\n========== DIFFERENCE DIRECTIONS ==========")

for name, column in [
    ("GBPQ-Mg", "Difference_Mg"),
    ("GBPQ-Fe", "Difference_Fe")
]:

    print(f"\n{name}")

    print(
        "Positive differences:",
        (df[column] > 0).sum()
    )

    print(
        "Negative differences:",
        (df[column] < 0).sum()
    )

    print(
        "Zero differences:",
        (df[column] == 0).sum()
    )

# ------------------------------------------------------------
# 6. SAVE RESULTS
# ------------------------------------------------------------

results.to_csv(
    OUTPUT_DIR / "07_pressure_comparison_metrics.csv"
)

df.to_csv(
    PROJECT_DIR / "results" /
    "07_pressure_differences.csv",
    index=False
)

print("\nSTEP 7 COMPLETED")
