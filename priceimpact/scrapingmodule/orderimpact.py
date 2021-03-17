from priceimpact.scrapingmodule import  DataStream as ds
import  pandas as pd
import numpy as np
import time
from priceimpact.models import orderdeltamodel


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



def endless_loop():
    while True:
        data = ds.get_order_data("BTCUSDT")
        model = orderdeltamodel(qty= data['qty'],buy= data['isBuyerMaker'],time= data['time'])
        model.save()
        time.sleep(2)


