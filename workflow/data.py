""" Download and cash the Fremont data

parameters
-----------------
filename = string (optional)
    location to save the Data
url = string (optional)
        location of the data
forced_download = Boolean (optional)
    if true, force redownload data

Returns
-------------
data: Pandas DataFrame
        The Fremont Bridge Dataset
"""
# Dataset: Seatle Fremont Bridge bike crossings from 2013 to 2019
import pandas as pd
from urllib.request import urlretrieve
import os
import matplotlib.pyplot as plt
plt.style.use('seaborn')
Fremont_url= 'https://data.seattle.gov/api/views/65db-xm6k/rows.csv?accessType=DOWNLOAD'


def get_fremont_data(filename='Fremont.csv', url=Fremont_url,
                     forced_download = False):

    if forced_download or not os.path.exists(filename):
        urlretrieve(url, 'Fremont.csv')
    data = pd.read_csv('Fremont.csv', index_col = 'Date')
    try:
        data.index = pd.to_datetime(data.index, format='%m/%d/%Y %I:%M:%S %p')
    except TypeError:
        data.index= pd.to_datetime(data.index)

    data.columns = ['West', 'East']
    data['Total'] = data['West'] + data['East']
    return data
