import pandas as pd
import datetime
import matplotlib.pyplot as plt
import seaborn as sns
from matplotlib.pylab import style
from statsmodels.tsa.arima_model import ARIMA
from statsmodels.graphics.tsaplots import plot_acf, plot_pacf

style.use('ggplot')
plt.rcParams['font.sans-serif'] = ['SimHei']
plt.rcParams['axes.unicode_minus'] = False

df = pd.read_csv('datas.csv')

train = df[0:10392]
test = df[10392:]

train.Timestamp = pd.to_datetime(train.Timestamp, format='%d-%m-%Y %H:%M')
train.index = train.Timestamp

train = train.resample('D').mean()

test.Timestamp = pd.to_datetime(test.Datetime, format='%d-%m-%Y %H:%M')

test.index = test.Timestamp

test = test.resample('D').mean()

# 图形设置

plt.figure(figsize=(16, 8))

plt.plot(train.index, train['Count'], label='Train')

plt.plot(test.index, test['Count'], label='Test')

plt.legend(loc='best')

plt.title("销售额走势")

plt.show()
