# NIFTY Volatility Alpha Engine

![CI](https://github.com/Rajputmansi7/NIFTY-Volatility-Alpha-Engine/actions/workflows/python-ci.yml/badge.svg)
![Python](https://img.shields.io/badge/Python-3.11-blue)
![Quant Finance](https://img.shields.io/badge/Domain-Quant%20Finance-black)
![ML](https://img.shields.io/badge/ML-XGBoost%20%7C%20LightGBM-orange)
![Status](https://img.shields.io/badge/Build-Passing-brightgreen)
![License](https://img.shields.io/badge/License-MIT-green)

## Institutional-Grade NIFTY Options Analytics & Volatility Signal Engine

A production-style quantitative finance project built using **NSE derivatives data**, **machine learning**, and **systematic backtesting** to generate actionable options trading signals for **NIFTY Index options**.

Designed to simulate the type of research infrastructure used by hedge funds, prop desks, and systematic trading teams.

---

## Project Highlights

* Live / historical NIFTY market data ingestion
* NSE option chain analytics
* IV Rank / IV Percentile engine
* Put-Call Ratio (PCR) signals
* Open Interest build-up / unwinding detection
* Realized vs Implied Volatility spreads
* Weekly expiry behavior modeling
* ML-based alpha prediction engine
* Strategy signal allocator
* Portfolio backtesting + risk analytics
* Interactive Streamlit dashboard
* Dockerized deployment ready
* CI/CD via GitHub Actions

---

## Quant Features Engine

### Volatility Signals

* Implied Volatility (ATM / strike-wise)
* IV Rank (1Y percentile)
* IV Percentile
* Volatility Smile / Skew
* Realized Volatility (5D / 10D / 20D)
* RV vs IV Mispricing Spread

### Positioning Signals

* Put Call Ratio (OI / Volume)
* OI Build-up Detection
* Long Unwinding / Short Covering
* Max Pain Levels
* Strike Concentration Zones

### Expiry Signals

* Days to Expiry
* Theta Crush Zones
* Weekly Expiry Regime Detection
* Monday-Friday Seasonal Effects

---

## Machine Learning Stack

Models supported:

* XGBoost
* LightGBM
* Random Forest
* LSTM (extensible)

Targets:

* Directional move prediction
* Volatility expansion prediction
* Range-bound probability
* Strategy regime classification

---

## Strategy Engine

Automatically allocates suitable options strategies:

* Long Straddle
* Short Straddle
* Iron Condor
* Bull Call Spread
* Bear Put Spread
* No Trade Filter

---

## Backtesting Metrics

* CAGR
* Sharpe Ratio
* Sortino Ratio
* Max Drawdown
* Win Rate
* Trade Expectancy
* Equity Curve

---

## Repository Structure

```text
NIFTY-Volatility-Alpha-Engine/
├── .github/workflows/python-ci.yml
├── assets/
├── dashboard/
│   └── app.py
├── data/
├── notebooks/
├── src/
│   ├── fetch_data.py
│   ├── live_nse.py
│   ├── features.py
│   ├── model.py
│   ├── allocator.py
│   ├── signals.py
│   ├── backtest.py
│   └── performance.py
├── requirements.txt
├── Dockerfile
├── main.py
└── README.md
```

---

## Installation

```bash
git clone https://github.com/Rajputmansi7/NIFTY-Volatility-Alpha-Engine.git
cd NIFTY-Volatility-Alpha-Engine
pip install -r requirements.txt
```

---

## Run Locally

```bash
python main.py
```

## Launch Dashboard

```bash
streamlit run dashboard/app.py
```

---

## Docker Deployment

```bash
docker build -t nifty-alpha .
docker run -p 8501:8501 nifty-alpha
```

---

## CI/CD

GitHub Actions automatically:

* Installs dependencies
* Validates build
* Runs project pipeline on push
* Ensures production readiness

---

## Resume Value

This project demonstrates:

* Quantitative Finance Knowledge
* Derivatives / Options Understanding
* Applied Machine Learning
* Time Series Modeling
* Production Engineering
* Risk Analytics
* Dashboard Development

---

## Sample Resume Bullet

Built an institutional-grade NIFTY options volatility signal engine using NSE option-chain data, machine learning models, and systematic backtesting with Sharpe-focused strategy allocation.

---

## Future Enhancements

* Greeks Engine
* Black-Scholes Pricing
* Monte Carlo Simulation
* Reinforcement Learning Strategy Selector
* Order Flow Analytics
* Cloud Deployment (AWS/GCP)

---

## Author

**Mansi Rajput**

If this repo helped you, feel free to star it.
