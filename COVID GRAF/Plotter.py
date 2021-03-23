import pandas as pd
import matplotlib.pyplot as plt
import matplotlib as mpl


categories = {0: "confirmed", 1: "deaths", 2: "recovered"}

print("Chose category")
for cat in categories.items():
    print('{} - {}'.format(cat[0], cat[1]))

category = categories[int(input())]

print("Wait...")
cases = pd.read_csv('https://data.humdata.org/hxlproxy/data/download/time_series_covid19_' + category + '_global_narrow.csv?dest=data_edit&filter01=merge&merge-url01=https%3A%2F%2Fdocs.google.com%2Fspreadsheets%2Fd%2Fe%2F2PACX-1vTglKQRXpkKSErDiWG6ycqEth32MY0reMuVGhaslImLjfuLU0EUgyyu2e-3vKDArjqGX7dXEBV8FJ4f%2Fpub%3Fgid%3D1326629740%26single%3Dtrue%26output%3Dcsv&merge-keys01=%23country%2Bname&merge-tags01=%23country%2Bcode%2C%23region%2Bmain%2Bcode%2C%23region%2Bsub%2Bcode%2C%23region%2Bintermediate%2Bcode&filter02=merge&merge-url02=https%3A%2F%2Fdocs.google.com%2Fspreadsheets%2Fd%2Fe%2F2PACX-1vTglKQRXpkKSErDiWG6ycqEth32MY0reMuVGhaslImLjfuLU0EUgyyu2e-3vKDArjqGX7dXEBV8FJ4f%2Fpub%3Fgid%3D398158223%26single%3Dtrue%26output%3Dcsv&merge-keys02=%23adm1%2Bname&merge-tags02=%23country%2Bcode%2C%23region%2Bmain%2Bcode%2C%23region%2Bsub%2Bcode%2C%23region%2Bintermediate%2Bcode&merge-replace02=on&merge-overwrite02=on&filter03=explode&explode-header-att03=date&explode-value-att03=value&filter04=rename&rename-oldtag04=%23affected%2Bdate&rename-newtag04=%23date&rename-header04=Date&filter05=rename&rename-oldtag05=%23affected%2Bvalue&rename-newtag05=%23affected%2Binfected%2Bvalue%2Bnum&rename-header05=Value&filter06=clean&clean-date-tags06=%23date&filter07=sort&sort-tags07=%23date&sort-reverse07=on&filter08=sort&sort-tags08=%23country%2Bname%2C%23adm1%2Bname&tagger-match-all=on&tagger-default-tag=%23affected%2Blabel&tagger-01-header=province%2Fstate&tagger-01-tag=%23adm1%2Bname&tagger-02-header=country%2Fregion&tagger-02-tag=%23country%2Bname&tagger-03-header=lat&tagger-03-tag=%23geo%2Blat&tagger-04-header=long&tagger-04-tag=%23geo%2Blon&header-row=1&url=https%3A%2F%2Fraw.githubusercontent.com%2FCSSEGISandData%2FCOVID-19%2Fmaster%2Fcsse_covid_19_data%2Fcsse_covid_19_time_series%2Ftime_series_covid19_' + category + '_global.csv', skiprows=[1])


print("Countries:")
countries = cases['Country/Region'].unique()
print("\n".join(countries))
print("Print name of country:")
country = [input()]
country_collum = country[0]

cases = cases[cases['Province/State'].isnull()]
cases = cases[cases['Country/Region'].isin(country)]
values = cases.pivot(index='Date', columns=['Country/Region'], values='Value')
print(cases)

dates = values.index.tolist()
values_delta = values.copy()
for i in range(len(dates)):
    if i == 0:
        values_delta.loc[dates[i], country_collum] = 0
    else:
        values_delta.loc[dates[i], country_collum] = values.loc[dates[i], country_collum] - values.loc[dates[i-1], country_collum]
print(cases)

plt.style.use('fivethirtyeight')

plot = values.plot(figsize=(8, 6), linewidth=2, )
plot.legend(prop={'size': 6})

plot2 = values_delta.plot(figsize=(8, 6), linewidth=2, )
plot2.legend(prop={'size': 6})

plt.show()