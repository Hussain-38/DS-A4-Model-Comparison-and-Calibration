# -*- coding: utf-8 -*-
"""
Created on Mon Nov  9 16:47:22 2026

@author: hussa
"""


# =====================================================
# DS-A4: MODEL COMPARISON AND CALIBRATION LAB
# STEP 2: LOAD THE DATASET
# =====================================================

import pandas as pd
from pathlib import Path

# 1. Define dataset location

PROJECT_DIR = Path(
    r"D:\Data Science Assignment\My Projects\DS-A4"
)

DATA_PATH = PROJECT_DIR / "raw dataset" / "S3.xls"

# 2. Load Excel dataset

df = pd.read_excel(
    DATA_PATH,
    sheet_name=0,
    engine="xlrd"
)

# 3. Display dataset information

print("\n========== DATASET INFORMATION ==========")

print("\nDataset dimensions:")
print(df.shape)

print("\nNumber of observations:", df.shape[0])

print("Number of columns:", df.shape[1])

# 4. Display first five observations

print("\n========== FIRST FIVE OBSERVATIONS ==========")

print(df.head())

# 5. Display all column names

print("\n========== COLUMN NAMES ==========")

for i, column in enumerate(df.columns, start=1):
    print(i, ":", column)

# 6. Display dataset information

print("\n========== DATA TYPES ==========")

df.info()

print("\nSTEP 2 COMPLETED")
