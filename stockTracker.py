#Source:  https://www.youtube.com/watch?v=JwSS70SZdyM

import yfinance as yf
import streamlit as st
import pandas as pd

st.write("""
# Simple Stock Price App

Shown are the stock closing price and volume of **Cisco**

""")

tickerSym = 'CSCO'

tickerData = yf.Ticker(tickerSym)

tickerDf = tickerData.history(period='1d', start='2020-1-20', end='2021-1-20')
 

# Open  High    Low     Close   Volume      Dividends   Stock Splits

st.line_chart(tickerDf.Close)
st.line_chart(tickerDf.Volume)

