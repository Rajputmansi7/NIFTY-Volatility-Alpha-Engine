import requests, pandas as pd

HEADERS={"User-Agent":"Mozilla/5.0"}
URL='https://www.nseindia.com/api/option-chain-indices?symbol=NIFTY'

def fetch_option_chain():
    s=requests.Session()
    s.get('https://www.nseindia.com',headers=HEADERS,timeout=10)
    r=s.get(URL,headers=HEADERS,timeout=10)
    data=r.json()['records']['data']
    rows=[]
    for x in data:
        strike=x.get('strikePrice')
        ce=x.get('CE',{})
        pe=x.get('PE',{})
        rows.append({
            'strike':strike,
            'call_oi':ce.get('openInterest',0),
            'put_oi':pe.get('openInterest',0),
            'call_iv':ce.get('impliedVolatility',0),
            'put_iv':pe.get('impliedVolatility',0)
        })
    return pd.DataFrame(rows)