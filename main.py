import streamlit as st, pandas as pd, numpy as np, yfinance as yf
import plotly.express as px
import datetime as dt

st.title("Stock Dashboard")

ticker = st.sidebar.text_input("Ticker")
ticker_s = st.sidebar.selectbox("Ticker", ["AAPL", "MSFT", "WATT"])
# st.date_input(label, value=None, min_value=None, max_value=None, key=None, help=None, on_change=None, args=None, kwargs=None, *, disabled=False, label_visibility="visible")
start_date_dt = dt.date(2021, 5, 19)
start_date = st.sidebar.date_input("Start Date", value=start_date_dt)
end_date = st.sidebar.date_input("End Date")

data = yf.download(ticker_s, start=start_date, end=end_date)
fig = px.line(data, y=data["Adj Close"], title=ticker_s)  # x=data.index[]


tab1, tab2 = st.tabs(["📈 Chart", "🗃 Data"])

with tab1:
    st.subheader("Price chart")
    st.plotly_chart(fig)
# tab1.line_chart(data)

with tab2:
    st.subheader("Data")
    # st.write(data)
    data2 = data
    data2["% Change"] = data["Adj Close"] / data["Adj Close"].shift(1)
    data2.dropna(inplace=True)
    st.write(data2)


pricing_data, fundamental_data, news = st.tabs(
    ["Pricing Data", "Fundamental Data", "Top 10 News"]
)

with pricing_data:
    st.header("Price Movements")

    annual_return = data2["% Change"].mean() * 252 * 100
    st.write("Annual return is ", annual_return, "%")
    stdev = np.std(data2["% Change"]) * np.sqrt(252)
    st.write("Standard deviation is ", stdev * 100, "%")

with fundamental_data:
    st.header("Fundamentals Data")


with news:
    st.header("News")


st.divider()
# with fundamental_data:

st.header("Yield Curve")
st.markdown("Correction of inversion is actually __common__ just prior to a recession")
st.markdown("It's **not** an absolute indicator, though!")
