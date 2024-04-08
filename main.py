import streamlit as st
import pandas as pd
import altair as alt
@st.catche_data
def load_data(csv):
    df = pd.read_csv(csv)
    return df
stops = load_data("data/Officer_Traffic_Stops.csv")
age_bar = alt.Chart(stops).mark_bar().encode(
    alt.X("Driver_Age", bin=alt.Bin(maxbins=10)),
    y='cound()',
    tooltip=alt.Tooltip(['Driver_Age','count()'])
)
st.altair_chart(age_bar)

st.write('Tabarek was here!')