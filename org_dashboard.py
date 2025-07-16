import pandas as pd
import streamlit as st

df = pd.read_csv("data/org_metrics.csv")

st.title("Organizational Health Dashboard")
st.metric("Total Employees", len(df))
st.bar_chart(df.groupby("Department")["Headcount"].sum())
st.line_chart(df.set_index("Month")["Turnover Rate"])
