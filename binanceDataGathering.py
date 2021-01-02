# Docs: https://python-binance.readthedocs.io/en/latest/binance.html#binance.client.Client.get_klines
import numpy as np
import requests

def close_data(array, coinname, interval):
    url = requests.get("https://api.binance.com/api/v3/klines?symbol="+coinname+"&interval="+interval+"&limit=500").json()
    url = np.array(url)
    closeData = 4 #In the fourth place of each entry is the close data
    for i in range(len(url)):
        array[i] = url[i, closeData]
