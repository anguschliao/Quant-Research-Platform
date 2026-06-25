# Quantitative Market Research Platform

![Python](https://img.shields.io/badge/Python-3.12-blue)
![Research](https://img.shields.io/badge/Status-Research-orange)
![Version](https://img.shields.io/badge/Version-v0.1.0-green)
![Active](https://img.shields.io/badge/Project-Active-brightgreen)

> A modular quantitative research framework for developing,
> evaluating, and deploying probabilistic models for systematic trading

---

## 🎯 Overview

This repository is a research-first platform for building statistical and machine learning models that estimate market proabilities rather than attempting deterministic price predictions

The framework supports experimentation with multiple model families - including Random Forests, Gradient Boosted Trees (XGBoost, LightGBM, CatBoost), Logistic Regression, Hidden Markov Models, and ensemble learning - within a reproducible research pipeline

Models are evaluated using both predictive metrics (ROC AUC, calibration, log loss) and financial metrics (Sharpe ratio, expectancy, drawdown).



## 🔬Research Objectives

The primary objective is to estimate the conditional probabiliy

> **P̂(Yₜ₊ₕ = 1 │ Xₜ, Rₜ, Θ)**

where 

- **Yₜ₊ₕ** = future market outcome
- **Xₜ** = engineered feature vector
- **Rₜ** = inferred market regime
- **Θ** = learned model parameters and ensemble weights

The main question asked is:

"Given the current market state, what is the probability of a profitable outcome?"

## 🚀 Research Focus

- Probabilistic forecasting
- Feature engineering
- Market regime detection
- Ensemble learning
- Probability calibration
- Walk-forward validation
- Hyperparameter optimization
- Risk-adjusted signal generation
- Performance attrition

##  📊 Research Pipeline

```
Market Data 
    |
    ▼
Data Validation
    |
    ▼
Feature Engineering
    |
    ▼
Market Regime Detection
    |
    ▼
Machine Learning Models 
    |
    ▼
Probabilistic Calibration
    |
    ▼
Ensemble Learning
    |
    ▼
Risk Optimization
    |
    ▼
Backtesting
    |
    ▼
Trade Execution
```

## 📁Repo Structure

```
project/ 
│ 
├── src/ 
│ ├── data/ 
│ ├── features/ 
│ ├── models/ 
│ ├── training/ 
│ ├── ensemble/ 
│ ├── risk/ 
│ └── execution/ 
│ 
├── configs/ 
├── notebooks/ 
├── tests/ 
├── docs/ 
├── logs/ 
└── README.md
```

