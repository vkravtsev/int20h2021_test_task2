import numpy as np
import pandas as pd

df = pd.read_csv('data_analytics.csv', index_col=None)
df['Event Date'] = df['Event Date'].astype('datetime64')
df.insert(2, 'Week Number', df['Event Date'].dt.week)
df['Week Number'] = df['Week Number'] - 28
df['Week Number'] = df['Week Number'].astype('int')

countries = df['Country'].unique()
conversions_countries = {i: [] for i in countries}

for country in conversions_countries:
    for week in range(2, 7):
        conversions_countries[country].append(df[df['Country'] == country][df['Week Number'] == week]['Event Date'].count() /
                                    df[df['Country'] == country][df['Week Number'] == week - 1]['Event Date'].count())

ltv_countries = {i: 0 for i in countries}
for c in conversions_countries:
    for conv in conversions_countries[c]:
        proceeds = 9.99 * 0.7 * conv
        ltv_countries[c] += proceeds

conversions = []
for week in range(2, 7):
    conversions.append(df[df['Week Number'] == week]['Event Date'].count() /
                        df[df['Week Number'] == week - 1]['Event Date'].count())

ltv = 0

for i in conversions:
    proceeds1 = 9.99 * 0.7 * i
    ltv += proceeds1

print(f'LTV for all users = {ltv}')
print(f'Bar charts for LTV by countries: {ltv_countries}')


