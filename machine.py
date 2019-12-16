import pandas as pd
import numpy as np
import matplotlib.pylab as plt
plt.rcParams['figure.figsize'] = (16, 9)
plt.style.use('fast')



df = pd.read_csv('time_series.csv',  parse_dates=[0], header=None,index_col=0, squeeze=True,names=['fecha','unidades'])
print(df.index.min())
print(df.index.max())
#Muestras por año

print(len(df['2017']))
print(len(df['2018']))
print(df.describe())

meses =df.resample('M').mean()
print(meses)



verano2017 = df['2017-06-01':'2017-09-01']
plt.plot(verano2017.values)
verano2018 = df['2018-06-01':'2018-09-01']
plt.plot(verano2018.values)

plt.show()