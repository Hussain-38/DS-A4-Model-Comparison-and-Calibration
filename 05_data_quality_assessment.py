# -*- coding: utf-8 -*-
"""
Created on Mon Nov  9 16:56:22 2026

@author: hussa
"""


# ============================================================
# DS-A4: MODEL COMPARISON AND CALIBRATION LAB
# STEP 5: SCIENTIFIC DATA QUALITY ASSESSMENT
# ============================================================

import pandas as pd
import numpy as np
from pathlib import Path

# ------------------------------------------------------------
# 1. LOAD CORRECTED DATASET
# ------------------------------------------------------------

PROJECT_DIR = Path(
    r"D:\Data Science Assignment\My Projects\DS-A4"
)

DATA_PATH = PROJECT_DIR / "raw dataset" / "S3.xls"

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
# 2. CHECK DATA TYPES
# ------------------------------------------------------------

print("\n========== DATA TYPES ==========")

print(df.dtypes)

# ------------------------------------------------------------
# 3. CHECK MISSING VALUES
# ------------------------------------------------------------

print("\n========== MISSING VALUES ==========")

missing = pd.DataFrame({
    "Missing_Count": df.isnull().sum(),
    "Missing_Percentage": (
        df.isnull().mean() * 100
    )
})

print(missing)

# ------------------------------------------------------------
# 4. CHECK NUMERICAL VARIABLES
# ------------------------------------------------------------

numeric_columns = [
    "T_GB00_GASP",
    "P_GASP",
    "T_GB00_GBPQ",
    "P_GBPQ_Mg",
    "P_GBPQ_Fe",
    "Fe_Bt", "Mg_Bt", "AlVI_Bt", "Ti_Bt",
    "Ca_Pl", "Na_Pl", "K_Pl",
    "Fe_Grt", "Mg_Grt", "Ca_Grt", "Mn_Grt"
]

print("\n========== NUMERICAL SUMMARY ==========")

print(df[numeric_columns].describe().T)

# ------------------------------------------------------------
# 5. CHECK PHYSICAL PLAUSIBILITY
# ------------------------------------------------------------

print("\n========== PHYSICAL RANGE CHECK ==========")

for col in numeric_columns:

    print(
        f"{col}: "
        f"Minimum = {df[col].min():.4f}, "
        f"Maximum = {df[col].max():.4f}"
    )

# ------------------------------------------------------------
# 6. CHECK DUPLICATE OBSERVATIONS
# ------------------------------------------------------------

print("\n========== DUPLICATE CHECK ==========")

print(
    "Exact duplicate rows:",
    df.duplicated().sum()
)

print(
    "Repeated Source-Sample combinations:",
    df.duplicated(
        subset=["Source", "Sample"]
    ).sum()
)

# ------------------------------------------------------------
# 7. CHECK UNIQUE SOURCES
# ------------------------------------------------------------

print("\n========== SOURCE INFORMATION ==========")

print(
    "Unique research sources:",
    df["Source"].nunique()
)

print(
    "Unique sample identifiers:",
    df["Sample"].nunique()
)

# ------------------------------------------------------------
# 8. COMPARE THE TWO GB00 TEMPERATURE COLUMNS
# ------------------------------------------------------------

print("\n========== TEMPERATURE COMPARISON ==========")

temperature_difference = (
    df["T_GB00_GBPQ"] - df["T_GB00_GASP"]
)

print(
    "Mean temperature difference:",
    temperature_difference.mean()
)

print(
    "Mean absolute temperature difference:",
    temperature_difference.abs().mean()
)

print(
    "Maximum absolute temperature difference:",
    temperature_difference.abs().max()
)

# ------------------------------------------------------------
# 9. CHECK PRESSURE UNITS AND RANGES
# ------------------------------------------------------------

print("\n========== PRESSURE SUMMARY ==========")

pressure_columns = [
    "P_GASP",
    "P_GBPQ_Mg",
    "P_GBPQ_Fe"
]

print(df[pressure_columns].describe().T)

print("\nSTEP 5 COMPLETED")
