import streamlit as st
import yfinance as yf
import pandas as pd

st.set_page_config(page_title="Personal Finance Dashboard", layout="wide")

st.title("💹 Personal Finance & Budget Tracker")

# Tabs
tab1, tab2, tab3 = st.tabs(["Stocks", "Currencies", "Crypto"])

# --- STOCKS TAB ---
with tab1:
    st.subheader("📈 Stock Prices")

    stock_symbol = st.text_input("Enter a stock symbol (e.g. AAPL, MSFT, TSLA):", key="stock")
    if st.button("Get Stock Data", key="stock_btn"):
        if stock_symbol:
            stock = yf.Ticker(stock_symbol.upper())
            data = stock.history(period="5d")

            if not data.empty:
                st.metric(label=f"Current Price ({stock_symbol.upper()})", value=f"${data['Close'][-1]:.2f}")
                st.line_chart(data['Close'])
            else:
                st.warning("No data found for this symbol.")
        else:
            st.warning("Please enter a stock symbol.")

# --- CURRENCIES TAB ---
with tab2:
    st.subheader("💱 Currency Exchange Rates (vs USD)")

    currency_code = st.text_input("Enter a currency code (e.g. EUR, GBP, JPY, TRY):", key="currency")
    if st.button("Get Currency Data", key="currency_btn"):
        if currency_code:
            pair = currency_code.upper() + "USD=X"
            currency = yf.Ticker(pair)
            data = currency.history(period="5d")

            if not data.empty:
                st.metric(label=f"Current Rate ({currency_code.upper()}/USD)", value=f"${data['Close'][-1]:.4f}")
                st.line_chart(data['Close'])
            else:
                st.warning("No data found for this currency.")
        else:
            st.warning("Please enter a currency code.")

# --- CRYPTO TAB ---
with tab3:
    st.subheader("🪙 Cryptocurrency Prices (vs USD)")

    crypto_code = st.text_input("Enter a cryptocurrency symbol (e.g. BTC, ETH, SOL):", key="crypto")
    if st.button("Get Crypto Data", key="crypto_btn"):
        if crypto_code:
            pair = crypto_code.upper() + "-USD"
            crypto = yf.Ticker(pair)
            data = crypto.history(period="5d")

            if not data.empty:
                st.metric(label=f"Current Price ({crypto_code.upper()}/USD)", value=f"${data['Close'][-1]:.2f}")
                st.line_chart(data['Close'])
            else:
                st.warning("No data found for this crypto.")
        else:
            st.warning("Please enter a crypto symbol.")
