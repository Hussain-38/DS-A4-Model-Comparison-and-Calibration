# -*- coding: utf-8 -*-
"""
Created on Mon Nov  9 16:44:05 2026

@author: hussa
"""


# =====================================================
# DS-A4: MODEL COMPARISON AND CALIBRATION LAB
# STEP 1: PROJECT SETUP
# =====================================================

from pathlib import Path

# 1. Define the main project directory

PROJECT_DIR = Path(
    r"D:\Data Science Assignment\My Projects\DS-A4"
)

# 2. Define the dataset directory

DATA_DIR = PROJECT_DIR / "raw dataset"

# 3. Find the Excel dataset

excel_files = list(DATA_DIR.glob("*.xls"))

print("========== PROJECT SETUP ==========")

print("Project directory:", PROJECT_DIR)
print("Dataset directory:", DATA_DIR)

print("\nExcel files found:")

for file in excel_files:
    print(file.name)

# 4. Check whether the directory exists

print("\nDataset folder exists:", DATA_DIR.exists())

# 5. Check whether the Excel file exists

if len(excel_files) == 0:
    raise FileNotFoundError(
        "No .xls file found in the dataset folder."
    )

print("\nNumber of Excel files:", len(excel_files))

print("\nSTEP 1 COMPLETED")
