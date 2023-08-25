import time
import datetime
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import requests

import matplotlib as mpl

filename_1m = 'future_df_ok_1m_me.csv'
data_1m = pd.read_csv(filename_1m, index_col=0)
# data_1m['open_time'] = pd.to_datetime(data_1m['open_time'], unit="ms") + pd.Timedelta(hours=8)
print(len(data_1m))

filename_30m = 'future_df_ok_1m_5.4.csv'
data_2 = pd.read_csv(filename_30m, index_col=0)
print(len(data_2))
# data_2['open_time'] = pd.to_datetime(data_2['open_time'], unit="ms") + pd.Timedelta(hours=8)

all_df = pd.concat([data_1m, data_2])


all_df.drop_duplicates(subset='open_time',keep='first',inplace=True)
df_all = all_df.sort_values('open_time')
print(len(df_all))

df_all.to_csv('new_1m_ok_me.csv')
