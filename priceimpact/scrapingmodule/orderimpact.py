from priceimpact.scrapingmodule import  DataStream as ds
import  pandas as pd
import numpy as np

df = ds.get_order_data("BTCUSDT")
series = df[['qty','isBuyerMaker']]

def calculateDelta(data):
    sells = data.loc[data['isBuyerMaker'] == True]
    buys = data.loc[data['isBuyerMaker'] == False]
    buysum = pd.to_numeric(buys['qty'],downcast='float').values.sum()
    sellsum = pd.to_numeric(sells['qty'],downcast='float').values.sum()
    delta = buysum-sellsum

    return delta

def rollingorderimpact(empytylist,delta):
    array = np.roll(empytylist,-1)
    array[len(array)-1] = delta
    return array




