import streamlit as st
import pandas as pd
import os

st.set_page_config(page_title="AI Data Pipeline Monitoring", layout="wide")

st.title("🚀 AI Data Pipeline Monitoring Dashboard")

df = pd.read_csv("data/clean_sales.csv")

col1, col2, col3 = st.columns(3)

col1.metric("Total Records", len(df))
col2.metric("Total Sales", df["amount"].sum())
col3.metric("Average Sale", round(df["amount"].mean(), 2))

st.divider()

st.subheader("Processed Data")
st.dataframe(df)

st.divider()

st.subheader("Sales Distribution")
#st.bar_chart(df.set_index("customer_name")["amount"])
sales_by_customer = df.groupby("customer_name")["amount"].sum()
st.bar_chart(sales_by_customer)
st.divider()

st.subheader("Pipeline Logs")
import os

st.divider()
#st.subheader("Pipeline Logs")

if os.path.exists("logs/pipeline.log"):
    with open("logs/pipeline.log", "r") as f:
        logs = f.read()

    st.code(logs)
else:
    st.warning("No log file found yet.")
