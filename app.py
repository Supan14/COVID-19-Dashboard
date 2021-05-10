import streamlit as st
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import plotly.express as px
def main():
	df = load_data()
	st.title('covid-19 country-wise tracking and comparison')
	countries = df.Country.unique()
	selected_countries = st.sidebar.multiselect('Select Countries to compare', countries)
	if selected_countries:
		subset_df = df[df.Country.isin(selected_countries)]
	else:
		subset_df = df[df.Country.isin(['India'])]
	fig = px.line(subset_df, x="Date", y="Confirmed", color='Country')
	st.write(fig)
@st.cache
def load_data():
	return pd.read_csv('https://raw.githubusercontent.com/datasets/covid-19/master/data/countries-aggregated.csv')
if __name__ == '__main__':
	main()