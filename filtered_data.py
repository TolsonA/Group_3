import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import plotly.express as px
import seaborn as sns

df_data = pd.read_csv('data.csv')
df_data = df_data.drop(columns=['Unnamed: 60', 'Country Code', '2015'])

df_france = df_data[df_data['Country Name'].str.contains('France')]
df_japan = df_data[df_data['Country Name'].str.contains("Japan")]
df_canada = df_data[df_data['Country Name'].str.contains("Canada")]
df_cyprus = df_data[df_data['Country Name'].str.contains("Cyprus")]

df_countries = pd.concat([df_canada, df_cyprus, df_france, df_japan])

