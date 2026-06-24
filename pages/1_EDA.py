import streamlit as st
import pandas as pd
import plotly.express as px

st.title("📊 Exploratory Data Analysis")

df = pd.read_csv(
    "insurance.csv"
)

st.dataframe(
    df.head()
)

fig = px.histogram(
    df,
    x="charges",
    title="Charges Distribution"
)

st.plotly_chart(
    fig,
    use_container_width=True
)

fig2 = px.scatter(
    df,
    x="age",
    y="charges",
    color="smoker"
)

st.plotly_chart(
    fig2,
    use_container_width=True
)