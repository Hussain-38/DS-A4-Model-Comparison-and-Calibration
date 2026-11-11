# DS-A4: Model Comparison and Calibration

## Research Project

This project investigates the prediction of disagreement between GBPQ and GASP barometric estimates using machine-learning classification models and mineral-composition data.

The study compares three classification algorithms, evaluates predictive performance under class imbalance, examines probability calibration, and investigates threshold-dependent decision costs.

## Research Objectives

- Investigate the predictive information contained in mineral-composition variables.
- Compare Logistic Regression, Random Forest, and Gradient Boosting.
- Evaluate discrimination and probability calibration.
- Investigate threshold selection under different false-negative cost assumptions.
- Assess model uncertainty using paired source-cluster bootstrap resampling.
- Examine prediction errors across geological rock types.

## Dataset

The modelling dataset contains 2,084 observations and 11 mineral-composition predictors.

Predictors include:

- Biotite: Fe_Bt, Mg_Bt, AlVI_Bt, Ti_Bt
- Plagioclase: Ca_Pl, Na_Pl, K_Pl
- Garnet: Fe_Grt, Mg_Grt, Ca_Grt, Mn_Grt

The classification targets are Mg_10 and Fe_10.

Positive-class prevalence:

| Target | Positive cases | Prevalence |
|---|---:|---:|
| Mg_10 | 96 | 4.61% |
| Fe_10 | 45 | 2.16% |

## Methodology

The analysis includes:

1. Data inspection and quality assessment.
2. Pressure-disagreement analysis.
3. Source-level grouping and cross-validation.
4. Mineral assemblage classification and auditing.
5. Model comparison using three classifiers.
6. Out-of-fold performance evaluation.
7. Probability calibration diagnostics.
8. Threshold and cost sensitivity analysis.
9. Rock-type error-slice analysis.
10. Paired source-cluster bootstrap with 1,000 replicates.
11. Reproducibility and submission auditing.

## Model Performance

| Target | Model | PR-AUC | ROC-AUC | Brier |
|---|---|---:|---:|---:|
| Mg_10 | Logistic Regression | 0.1109 | 0.7620 | 0.0438 |
| Mg_10 | Random Forest | 0.2359 | 0.8631 | 0.0389 |
| Mg_10 | Gradient Boosting | 0.2218 | 0.8031 | 0.0396 |
| Fe_10 | Logistic Regression | 0.1024 | 0.8376 | 0.0209 |
| Fe_10 | Random Forest | 0.2090 | 0.8764 | 0.0190 |
| Fe_10 | Gradient Boosting | 0.2378 | 0.7812 | 0.0188 |

Random Forest achieved the highest PR-AUC for Mg_10, while Gradient Boosting achieved the highest PR-AUC for Fe_10.

## Results and Figures

Diagnostic figures and cost curves are available in `results/figures/`.

Processed datasets, model metrics, bootstrap results, and other analysis tables are available in `results/tables/`.

## Project Structure

```text
DS-A4-Model-Comparison-and-Calibration/
│
├── README.md
├── DS-A4_Final_Report.pdf
├── 01–33 Python analysis scripts
├── 29_final_audit.txt
│
└── results/
    ├── figures/
    └── tables/
```

## Reproducibility

The project was developed using:

- Python 3.12.7
- pandas 3.0.6
- NumPy 2.4.6
- scikit-learn 1.9.1
- Matplotlib 3.11.1

The project includes analysis scripts, processed outputs, diagnostic figures, and a reproducibility audit.

The original source dataset is not distributed in this repository. Reproducing the complete workflow requires access to the appropriately licensed input data.

## Limitations

- Both classification targets have substantial class imbalance.
- GASP is used as a comparator, not independently verified geological ground truth.
- Independent external validation remains necessary.
- Rock-type subgroup sizes are uneven.
- Threshold-dependent costs are based on illustrative assumptions.

## Final Report

The complete academic report is available here:

**DS-A4_Final_Report.pdf**

## Author

Hussain-38

GitHub: https://github.com/Hussain-38/DS-A4-Model-Comparison-and-Calibration
