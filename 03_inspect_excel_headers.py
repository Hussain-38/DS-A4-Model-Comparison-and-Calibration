# -*- coding: utf-8 -*-
"""
Created on Mon Nov  9 16:49:37 2026

@author: hussa
"""


# =====================================================
# DS-A4: MODEL COMPARISON AND CALIBRATION LAB
# STEP 3: INSPECT ORIGINAL EXCEL HEADERS
# =====================================================

import pandas as pd
from pathlib import Path

# 1. Dataset location

PROJECT_DIR = Path(
    r"D:\Data Science Assignment\My Projects\DS-A4"
)

DATA_PATH = PROJECT_DIR / "raw dataset" / "S3.xls"

# 2. Read Excel WITHOUT assigning column names

raw = pd.read_excel(
    DATA_PATH,
    sheet_name=0,
    header=None,
    engine="xlrd"
)

# 3. Display the first four original Excel rows

print("\n========== ORIGINAL EXCEL STRUCTURE ==========")

print("Original dimensions:", raw.shape)

print("\nFirst four rows:")

print(raw.head(4).to_string(index=True))

# 4. Inspect the first two rows separately

print("\n========== FIRST ROW ==========")

for i, value in enumerate(raw.iloc[0]):
    print(f"Column {i}: {value}")

print("\n========== SECOND ROW ==========")

for i, value in enumerate(raw.iloc[1]):
    print(f"Column {i}: {value}")

print("\nSTEP 3 COMPLETED")
