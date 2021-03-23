import pandas as pd
import matplotlib.pyplot as plt
from matplotlib.dates import DateFormatter
import matplotlib.ticker as ticker

df = pd.read_csv('https://raw.githubusercontent.com/datasets/covid-19/master/data/countries-aggregated.csv', parse_dates=['Date'])
countries = ['Afghanistan', 'Belarus']
df = df[df['Country'].isin(countries)]

df['Cases'] = df[['Confirmed']].sum(axis=1)
df = df.pivot(index='Date', columns='Country', values='Cases')
countries = list(df.columns)
covid = df.reset_index('Date')
covid.set_index(['Date'], inplace=True)
covid.columns = countries

populations = {'Afghanistan': 37466414 , 'Belarus': 9450000}
num = covid.copy()
for country in list(num.columns):
    num[country] = num[country]/populations[country] * 100000

colors = {'Belarus':'#006E4A', 'Afghanistan':'#291ABB'}
plt.style.use('fivethirtyeight')

plot = covid.plot(figsize=(18,9), color=list(colors.values()), linewidth=7, legend=False)  
plot.yaxis.set_major_formatter(ticker.StrMethodFormatter('{x:,.0f}'))
plot.grid(color='#d4d4d4')
plot.set_xlabel('Date')
plot.set_ylabel('Num of Cases')

for country in list(colors.keys()):
    plot.text(x = covid.index[-1], y = covid[country].max(), color = colors[country], s = country, weight = 'bold')
    print(covid[country].max())

plt.show()
