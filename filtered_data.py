import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

df_data = pd.read_csv('data.csv')

df_france = df_data[df_data['Country Name'].str.contains('France')]
df_japan = df_data[df_data['Country Name'].str.contains("Japan")]
df_canada = df_data[df_data['Country Name'].str.contains("Canada")]
df_cyprus = df_data[df_data['Country Name'].str.contains("Cyprus")]

df_countries = pd.concat([df_canada, df_cyprus, df_france, df_japan])

