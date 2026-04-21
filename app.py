import streamlit as st
import plotly.express as px
import pandas as pd
import numpy as np

st.set_page_config(layout='wide')
st.title('NIFTY Quant Hedge Fund Alpha Engine')

col1,col2,col3,col4=st.columns(4)
col1.metric('Signal','IRON_CONDOR')
col2.metric('IV Rank','84%')
col3.metric('Sharpe','1.92')
col4.metric('Drawdown','-8.4%')

x=pd.DataFrame({'day':range(100),'equity':np.cumprod(1+np.random.normal(.001,.01,100))})
fig=px.line(x,x='day',y='equity',title='Equity Curve')
st.plotly_chart(fig,use_container_width=True)