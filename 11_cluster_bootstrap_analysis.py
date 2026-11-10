
# ============================================================
# DS-A4: MODEL COMPARISON AND CALIBRATION LAB
# STEP 11: OPTIMIZED SOURCE-CLUSTER BOOTSTRAP
# ============================================================

import pandas as pd
import numpy as np
from pathlib import Path

# ------------------------------------------------------------
# 1. CONFIGURATION
# ------------------------------------------------------------

PROJECT_DIR = Path(
    r"D:\Data Science Assignment\My Projects\DS-A4"
)

DATA_PATH = PROJECT_DIR / "raw dataset" / "S3.xls"

OUTPUT_DIR = PROJECT_DIR / "results" / "tables"
OUTPUT_DIR.mkdir(parents=True, exist_ok=True)

SEED = 42
N_BOOTSTRAP = 2000

rng = np.random.default_rng(SEED)

# ------------------------------------------------------------
# 2. LOAD DATASET
# ------------------------------------------------------------

print("\nLoading dataset...")

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
# 3. CONVERT TO NUMPY ARRAYS
# ------------------------------------------------------------

d_mg = (
    df["P_GBPQ_Mg"].to_numpy(dtype=float)
    - df["P_GASP"].to_numpy(dtype=float)
)

d_fe = (
    df["P_GBPQ_Fe"].to_numpy(dtype=float)
    - df["P_GASP"].to_numpy(dtype=float)
)

# Convert Source to ordinary NumPy strings

sources = df["Source"].astype(str).to_numpy(dtype=str)

unique_sources, source_codes = np.unique(
    sources,
    return_inverse=True
)

n_sources = len(unique_sources)

print("Observations:", len(df))
print("Unique sources:", n_sources)

# ------------------------------------------------------------
# 4. OBSERVED METRICS
# ------------------------------------------------------------

def calculate_metrics(values):

    return {
        "Bias": np.mean(values),
        "MAE": np.mean(np.abs(values)),
        "RMSE": np.sqrt(np.mean(values ** 2))
    }

mg_observed = calculate_metrics(d_mg)
fe_observed = calculate_metrics(d_fe)

print("\n========== OBSERVED METRICS ==========")

print(pd.DataFrame({
    "GBPQ_Mg": mg_observed,
    "GBPQ_Fe": fe_observed
}).round(4))

# ------------------------------------------------------------
# 5. SOURCE-CLUSTER BOOTSTRAP
# ------------------------------------------------------------

print("\n========== RUNNING BOOTSTRAP ==========")

bootstrap_results = []

for iteration in range(N_BOOTSTRAP):

    # Sample research sources with replacement

    sampled_sources = rng.integers(
        0,
        n_sources,
        size=n_sources
    )

    # Count selections of each source

    source_counts = np.bincount(
        sampled_sources,
        minlength=n_sources
    )

    # Give every observation its source's bootstrap weight

    weights = source_counts[source_codes]

    total_weight = weights.sum()

    # GBPQ-Mg metrics

    mg_bias = np.sum(weights * d_mg) / total_weight

    mg_mae = np.sum(weights * np.abs(d_mg)) / total_weight

    mg_rmse = np.sqrt(
        np.sum(weights * d_mg**2) / total_weight
    )

    # GBPQ-Fe metrics

    fe_bias = np.sum(weights * d_fe) / total_weight

    fe_mae = np.sum(weights * np.abs(d_fe)) / total_weight

    fe_rmse = np.sqrt(
        np.sum(weights * d_fe**2) / total_weight
    )

    bootstrap_results.append([
        mg_bias,
        mg_mae,
        mg_rmse,
        fe_bias,
        fe_mae,
        fe_rmse,
        mg_mae - fe_mae
    ])

    if (iteration + 1) % 200 == 0:

        print(
            f"Completed {iteration + 1}/{N_BOOTSTRAP}"
        )

# ------------------------------------------------------------
# 6. CALCULATE CONFIDENCE INTERVALS
# ------------------------------------------------------------

columns = [
    "Mg_Bias",
    "Mg_MAE",
    "Mg_RMSE",
    "Fe_Bias",
    "Fe_MAE",
    "Fe_RMSE",
    "MAE_Mg_minus_Fe"
]

bootstrap_df = pd.DataFrame(
    bootstrap_results,
    columns=columns
)

summary = []

for metric in columns:

    lower = bootstrap_df[metric].quantile(0.025)

    upper = bootstrap_df[metric].quantile(0.975)

    summary.append({
        "Metric": metric,
        "Lower_95_CI": lower,
        "Upper_95_CI": upper
    })

ci_table = pd.DataFrame(summary)

# ------------------------------------------------------------
# 7. DISPLAY RESULTS
# ------------------------------------------------------------

print("\n========== 95% BOOTSTRAP CONFIDENCE INTERVALS ==========")

print(ci_table.round(4).to_string(index=False))

# ------------------------------------------------------------
# 8. SAVE RESULTS
# ------------------------------------------------------------

ci_table.to_csv(
    OUTPUT_DIR / "11_bootstrap_confidence_intervals.csv",
    index=False
)

bootstrap_df.to_csv(
    OUTPUT_DIR / "11_bootstrap_replicates.csv",
    index=False
)

print("\nBootstrap iterations:", N_BOOTSTRAP)
print("Research sources:", n_sources)

print("\nSTEP 11 COMPLETED")
