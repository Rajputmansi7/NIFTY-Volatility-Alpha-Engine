![CI](https://github.com/YOUR_USERNAME/YOUR_REPO/actions/workflows/python-ci.yml/badge.svg)
# NIFTY Quant Hedge Fund Alpha Engine

Institutional-grade options analytics platform for NIFTY derivatives using live NSE data, volatility regime detection, ML forecasting, and professional strategy backtesting.

## Institutional Features
- Live NSE option chain ingestion
- IV Surface / Smile / Skew analytics
- IV Rank / IV Percentile
- PCR OI + PCR Volume
- OI build-up / unwinding detection
- Weekly expiry regime engine
- XGBoost + LightGBM + LSTM models
- Ensemble alpha signals
- Options strategy allocator
- Full performance analytics (Sharpe / Sortino / MaxDD / CAGR)
- Streamlit quant dashboard
- Dockerized deployment

## Commands
pip install -r requirements.txt
python main.py
streamlit run dashboard/app.py
docker build -t nifty-alpha .
docker run -p 8501:8501 nifty-alpha
