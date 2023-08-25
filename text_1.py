import time
import datetime
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import requests

import matplotlib as mpl


filename_30m = 'future_df_ok_1m_5.4.csv'
data_2 = pd.read_csv(filename_30m, index_col=0)
print(len(data_2))

