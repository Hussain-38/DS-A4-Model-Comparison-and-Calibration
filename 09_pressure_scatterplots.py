# -*- coding: utf-8 -*-
"""
Created on Mon Nov  9 17:06:40 2026

@author: hussa
"""

# ============================================================
# DS-A4: MODEL COMPARISON AND CALIBRATION LAB
# STEP 9: PRESSURE COMPARISON SCATTER PLOTS
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
# 2. LOAD DATA
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
# 3. HELPER FUNCTION
# ------------------------------------------------------------

def make_scatter(ax, x, y, title):
    ax.scatter(x, y, alpha=0.45, s=18)

    min_val = min(x.min(), y.min())
    max_val = max(x.max(), y.max())

    ax.plot(
        [min_val, max_val],
        [min_val, max_val],
        linestyle="--",
        linewidth=1
    )

    correlation = np.corrcoef(x, y)[0, 1]

    ax.set_title(title)
    ax.set_xlabel("GASP pressure (kbar)")
    ax.set_ylabel("GBPQ pressure (kbar)")
    ax.text(
        0.05, 0.95,
        f"r = {correlation:.4f}",
        transform=ax.transAxes,
        verticalalignment="top"
    )

# ------------------------------------------------------------
# 4. CREATE SCATTER PLOTS
# ------------------------------------------------------------

fig, axes = plt.subplots(1, 2, figsize=(14, 6))

make_scatter(
    axes[0],
    df["P_GASP"],
    df["P_GBPQ_Mg"],
    "GASP vs GBPQ-Mg"
)

make_scatter(
    axes[1],
    df["P_GASP"],
    df["P_GBPQ_Fe"],
    "GASP vs GBPQ-Fe"
)

plt.suptitle(
    "Pressure Comparison of GBPQ Barometers Against GASP",
    fontsize=14
)

plt.tight_layout()

plt.savefig(
    FIGURE_DIR / "09_pressure_scatterplots.png",
    dpi=300,
    bbox_inches="tight"
)

plt.show()

# ------------------------------------------------------------
# 5. PRINT CORRELATIONS
# ------------------------------------------------------------

print("\n========== CORRELATION RESULTS ==========")

corr_mg = np.corrcoef(df["P_GASP"], df["P_GBPQ_Mg"])[0, 1]
corr_fe = np.corrcoef(df["P_GASP"], df["P_GBPQ_Fe"])[0, 1]

print(f"Correlation (GASP vs GBPQ-Mg): {corr_mg:.4f}")
print(f"Correlation (GASP vs GBPQ-Fe): {corr_fe:.4f}")

print("\nSTEP 9 COMPLETED")