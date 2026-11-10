# -*- coding: utf-8 -*-
"""
Created on Mon Nov  9 17:04:58 2026

@author: hussa
"""


# ============================================================
# DS-A4: MODEL COMPARISON AND CALIBRATION LAB
# STEP 8: BLAND-ALTMAN AGREEMENT ANALYSIS
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
# 3. DEFINE BLAND-ALTMAN FUNCTION
# ------------------------------------------------------------

def bland_altman(ax, reference, comparison, title):

    difference = comparison - reference

    average = (comparison + reference) / 2

    mean_difference = difference.mean()

    sd_difference = difference.std()

    upper_loa = mean_difference + 1.96 * sd_difference

    lower_loa = mean_difference - 1.96 * sd_difference

    # Scatter plot

    ax.scatter(
        average,
        difference,
        alpha=0.45,
        s=18
    )

    # Mean difference

    ax.axhline(
        mean_difference,
        linestyle="-",
        label=f"Mean bias = {mean_difference:.3f}"
    )

    # Limits of agreement

    ax.axhline(
        upper_loa,
        linestyle="--",
        label=f"Upper LoA = {upper_loa:.3f}"
    )

    ax.axhline(
        lower_loa,
        linestyle="--",
        label=f"Lower LoA = {lower_loa:.3f}"
    )

    ax.axhline(0, linestyle=":", linewidth=1)

    ax.set_title(title)

    ax.set_xlabel("Mean pressure (kbar)")

    ax.set_ylabel("Pressure difference (kbar)")

    ax.legend(fontsize=8)

    return {
        "Mean_Bias": mean_difference,
        "SD": sd_difference,
        "Upper_LoA": upper_loa,
        "Lower_LoA": lower_loa
    }

# ------------------------------------------------------------
# 4. CREATE TWO BLAND-ALTMAN PLOTS
# ------------------------------------------------------------

fig, axes = plt.subplots(
    1, 2,
    figsize=(14, 5)
)

mg_results = bland_altman(
    axes[0],
    df["P_GASP"],
    df["P_GBPQ_Mg"],
    "GBPQ-Mg versus GASP"
)

fe_results = bland_altman(
    axes[1],
    df["P_GASP"],
    df["P_GBPQ_Fe"],
    "GBPQ-Fe versus GASP"
)

plt.suptitle(
    "Bland-Altman Analysis of Barometer Agreement",
    fontsize=14
)

plt.tight_layout()

plt.savefig(
    FIGURE_DIR / "08_bland_altman_comparison.png",
    dpi=300,
    bbox_inches="tight"
)

plt.show()

# ------------------------------------------------------------
# 5. PRINT AGREEMENT STATISTICS
# ------------------------------------------------------------

print("\n========== BLAND-ALTMAN RESULTS ==========")

print("\nGBPQ-Mg:")

for key, value in mg_results.items():
    print(f"{key}: {value:.4f}")

print("\nGBPQ-Fe:")

for key, value in fe_results.items():
    print(f"{key}: {value:.4f}")

print("\nSTEP 8 COMPLETED")
