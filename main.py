from alpha_vantage.timeseries import TimeSeries
import matplotlib.pyplot as plt
import pandas as pd
import os

ts = TimeSeries(key=os.environ['ALPHA_API_KEY'], output_format='pandas')

data, meta_data = ts.get_daily_adjusted(symbol='ASX:XRO', outputsize='full')
data.set_index(pd.to_datetime(data.index), inplace=True )
data['4. close'].plot()
plt.title('Intraday Times Series for the XRO stock (1 min)')
plt.show()
