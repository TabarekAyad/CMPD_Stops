import streamlit as st
import altair as alt
import pandas as pd

st.title("CMPD Traffic Stops")


@st.cache_data  # 👈 Add the caching decorator
def load_data(csv):
    df = pd.read_csv(csv)
    return df

stops = pd.read_csv("data/Officer_Traffic_Stops.csv")

boxplot_chart = alt.Chart(stops).mark_boxplot().encode(
    x='Was_a_Search_Conducted',
    y='Driver_Age'
).properties(width=400)


st.altair_chart(boxplot_chart)
