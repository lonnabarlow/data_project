import streamlit as st
import pandas as pd 
import numpy as np 
import matplotlib.pyplot as plt 
import seaborn as sns


st.title('Looking at the Data')

@st.experimental_memo
def get_csv(csv):
    return csv

demand_actuals = get_csv('demand_actuals.csv')
demand_forecast = get_csv('demand_forecasts_v2.csv')
inventory_actuals = get_csv('inventory_actuals.csv')
production_forecast = get_csv('production_forecast.csv')


@st.experimental_memo
def get_df(csv):
    return pd.read_csv(csv)

demand_actuals_df = get_df(demand_actuals)
demand_forecast_df = get_df(demand_forecast)
inventory_actuals_df = get_df(inventory_actuals)
production_forecast_df = get_df(production_forecast)

st.title("Wine Demand, Inventory & Forecasting")


st.subheader("Choose from list below to see tables")

with st.expander("click to see raw data of demand actuals"):
    st.write(demand_actuals_df)

with st.expander("click to see raw data of demand forecast"):
    st.write(demand_forecast_df)

inventory_check = st.checkbox('see inventory actuals data')

if inventory_check:
    st.write(inventory_actuals_df)

st.subheader("here are other ways you could structure this - ")

raw_data_option = st.selectbox('What data would you like to see?', ('demand actual', 'demand forecast', 'inventory actual', 'production forecast'))

if raw_data_option == 'demand actual':
    st.write(demand_actuals_df)
if raw_data_option == 'demand forecast':
    st.write(demand_forecast_df)
if raw_data_option == 'inventory actual':
    st.write(inventory_actuals_df) 
if raw_data_option == 'production forecast':
    st.write(production_forecast)    