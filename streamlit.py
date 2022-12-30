import pandas as pd
import streamlit as st

df = pd.read_csv('./data/kc_house_data.csv')

st.write(df.head())