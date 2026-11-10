# -*- coding: utf-8 -*-
"""
Created on Mon Nov  9 16:51:00 2026

@author: hussa
"""


# =====================================================
# DS-A4: MODEL COMPARISON AND CALIBRATION LAB
# STEP 4: CORRECT DATASET LOADING
# =====================================================

import pandas as pd
from pathlib import Path

# 1. Dataset location

PROJECT_DIR = Path(
    r"D:\Data Science Assignment\My Projects\DS-A4"
)

DATA_PATH = PROJECT_DIR / "raw dataset" / "S3.xls"

# 2. Load using the SECOND Excel row as header

df = pd.read_excel(
    DATA_PATH,
    sheet_name=0,
    header=1,
    engine="xlrd"
)

# 3. Remove completely empty separator columns

df = df.dropna(axis=1, how="all")

# 4. Assign unique names to the two temperature columns

df.columns = [
    "Source",
    "Rock",
    "Sample",
    "Al2SiO5",
    "Opaque",
    "T_GB00_GASP",
    "P_GASP",
    "T_GB00_GBPQ",
    "P_GBPQ_Mg",
    "P_GBPQ_Fe",
    "Fe_Bt",
    "Mg_Bt",
    "AlVI_Bt",
    "Ti_Bt",
    "Ca_Pl",
    "Na_Pl",
    "K_Pl",
    "Fe_Grt",
    "Mg_Grt",
    "Ca_Grt",
    "Mn_Grt"
]

# 5. Display corrected dataset information

print("\n========== CORRECTED DATASET ==========")

print("Dataset dimensions:", df.shape)

print("\nColumn names:")

print(df.columns.tolist())

print("\nFirst five observations:")

print(df.head())

# 6. Verify the pressure and temperature columns

print("\n========== PRESSURE AND TEMPERATURE ==========")

print(
    df[
        [
            "T_GB00_GASP",
            "P_GASP",
            "T_GB00_GBPQ",
            "P_GBPQ_Mg",
            "P_GBPQ_Fe"
        ]
    ].head()
)

print("\nSTEP 4 COMPLETED")
