# -*- coding: utf-8 -*-
"""
Created on Mon Nov  9 16:59:36 2026

@author: hussa
"""


# ============================================================
# DS-A4: MODEL COMPARISON AND CALIBRATION LAB
# STEP 6: INVESTIGATE DATA FLAGS
# ============================================================

import pandas as pd
from pathlib import Path

# ------------------------------------------------------------
# 1. LOAD DATA
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
# 2. INVESTIGATE EXACT DUPLICATES
# ------------------------------------------------------------

print("\n========== EXACT DUPLICATES ==========")

duplicates = df[
    df.duplicated(keep=False)
].copy()

print("Rows involved in exact duplicates:",
      len(duplicates))

print(duplicates.to_string(index=False))

duplicates.to_csv(
    OUTPUT_DIR / "06_exact_duplicates.csv",
    index=False
)

# ------------------------------------------------------------
# 3. INVESTIGATE REPEATED SOURCE-SAMPLE PAIRS
# ------------------------------------------------------------

print("\n========== REPEATED SOURCE-SAMPLE PAIRS ==========")

repeated = df[
    df.duplicated(
        subset=["Source", "Sample"],
        keep=False
    )
].copy()

print("Rows involved:", len(repeated))

print(
    repeated[
        ["Source", "Sample", "P_GASP",
         "P_GBPQ_Mg", "P_GBPQ_Fe"]
    ].to_string(index=False)
)

repeated.to_csv(
    OUTPUT_DIR / "06_repeated_source_samples.csv",
    index=False
)

# ------------------------------------------------------------
# 4. ORIGINAL CALIBRATION RANGE FLAGS
# ------------------------------------------------------------

print("\n========== CALIBRATION RANGE FLAGS ==========")

df["Outside_Temperature_Range"] = (
    (df["T_GB00_GASP"] < 515) |
    (df["T_GB00_GASP"] > 878)
)

df["Outside_Pressure_Range"] = (
    (df["P_GASP"] < 1.0) |
    (df["P_GASP"] > 11.4)
)

df["Outside_Any_Range"] = (
    df["Outside_Temperature_Range"] |
    df["Outside_Pressure_Range"]
)

print(
    "Outside temperature range:",
    df["Outside_Temperature_Range"].sum()
)

print(
    "Outside pressure range:",
    df["Outside_Pressure_Range"].sum()
)

print(
    "Outside either range:",
    df["Outside_Any_Range"].sum()
)

# ------------------------------------------------------------
# 5. SAVE OBSERVATION FLAGS
# ------------------------------------------------------------

df.to_csv(
    OUTPUT_DIR / "06_calibration_range_flags.csv",
    index=False
)

print("\nSTEP 6 COMPLETED")
