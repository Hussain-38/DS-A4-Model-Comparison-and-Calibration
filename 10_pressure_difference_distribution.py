# -*- coding: utf-8 -*-
"""
Created on Mon Nov  9 17:09:12 2026

@author: hussa
"""


# ============================================================
# DS-A4: MODEL COMPARISON AND CALIBRATION LAB
# STEP 10: PRESSURE DIFFERENCE DISTRIBUTIONS
# ============================================================

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from pathlib import Path

# ------------------------------------------------------------
# 1. PROJECT CONFIGURATION
# ------------------------------------------------------------

PROJECT_DIR = Path(
    r"D:\Data Science Assignment\My Projects\DS-A4"
)

DATA_PATH = PROJECT_DIR / "raw dataset" / "S3.xls"

FIGURE_DIR = PROJECT_DIR / "results" / "figures"
FIGURE_DIR.mkdir(parents=True, exist_ok=True)

# ------------------------------------------------------------
# 2. LOAD DATASET
# ------------------------------------------------------------

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
# 3. CALCULATE PRESSURE DIFFERENCES
# ------------------------------------------------------------

df["Difference_Mg"] = (
    df["P_GBPQ_Mg"] - df["P_GASP"]
)

df["Difference_Fe"] = (
    df["P_GBPQ_Fe"] - df["P_GASP"]
)

# ------------------------------------------------------------
# 4. CREATE DISTRIBUTION PLOTS
# ------------------------------------------------------------

fig, axes = plt.subplots(
    1, 2,
    figsize=(13, 5)
)

# GBPQ-Mg

axes[0].hist(
    df["Difference_Mg"],
    bins=35,
    edgecolor="black",
    alpha=0.75
)

axes[0].axvline(
    0,
    linestyle="--",
    linewidth=1.5,
    label="Perfect agreement"
)

axes[0].axvline(
    df["Difference_Mg"].mean(),
    linestyle="-",
    linewidth=1.5,
    label="Mean difference"
)

axes[0].set_title("GBPQ-Mg minus GASP")

axes[0].set_xlabel("Pressure difference (kbar)")

axes[0].set_ylabel("Frequency")

axes[0].legend()

# GBPQ-Fe

axes[1].hist(
    df["Difference_Fe"],
    bins=35,
    edgecolor="black",
    alpha=0.75
)

axes[1].axvline(
    0,
    linestyle="--",
    linewidth=1.5,
    label="Perfect agreement"
)

axes[1].axvline(
    df["Difference_Fe"].mean(),
    linestyle="-",
    linewidth=1.5,
    label="Mean difference"
)

axes[1].set_title("GBPQ-Fe minus GASP")

axes[1].set_xlabel("Pressure difference (kbar)")

axes[1].set_ylabel("Frequency")

axes[1].legend()

plt.suptitle(
    "Distribution of Pressure Differences",
    fontsize=14
)

plt.tight_layout()

plt.savefig(
    FIGURE_DIR / "10_pressure_difference_distribution.png",
    dpi=300,
    bbox_inches="tight"
)

plt.show()

# ------------------------------------------------------------
# 5. DISTRIBUTION STATISTICS
# ------------------------------------------------------------

print("\n========== DISTRIBUTION STATISTICS ==========")

for name, column in [
    ("GBPQ-Mg", "Difference_Mg"),
    ("GBPQ-Fe", "Difference_Fe")
]:

    print(f"\n{name}")

    print("Mean:", df[column].mean())

    print("Median:", df[column].median())

    print("Standard deviation:", df[column].std())

    print("Skewness:", df[column].skew())

    print("Kurtosis:", df[column].kurtosis())

print("\nSTEP 10 COMPLETED")
