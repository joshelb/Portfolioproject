import  requests,json
import pandas as pd
from datetime import  datetime

pd.set_option("display.max_rows", None, "display.max_columns", None)


def get_price_data(tick_interval,market):
    binance_price_data_link = 'https://api.binance.com/api/v1/klines?symbol='+market+'&interval='+tick_interval+'&limit='+"800"
    data = requests.get(binance_price_data_link)
    parsed_data = json.loads(data.text)
    df = pd.DataFrame(parsed_data,columns=['open_time','open','high','low','close','volume','close_time','quote_asset_volume','number_of_trades','taker_buy_base_asset_volume','Taker_buy_quote_asset_volume','Ignore'])
    return df

def get_order_data(market):
    binance_order_data_link = "https://fapi.binance.com/fapi/v1/trades?symbol="+ market
    data = requests.get(binance_order_data_link)
    parsed_data = json.loads(data.text)
    df = pd.DataFrame(parsed_data,columns=["id","price","qty","quoteQty","time","isBuyerMaker","isBestMatch"])
    print(1)
    return df


def get_funding_data():
    bitmex_funding_data_link =  "https://www.bitmex.com/api/v1/funding?symbol=XBTUSD&count=500&reverse=true"
    data = requests.get(bitmex_funding_data_link)
    parsed_data = json.loads(data.text)
    df = pd.DataFrame(parsed_data,columns=["timestamp","symbol","fundingInterval","fundingRate","fundingRateDaily"])
    return df



"""def create_constant_funding_dataframe(funding_dataframe, price_object):
    for item in len(price_object):
        if(funding_dataframe["timestamp"][item+1]>price_object["close_time"]>funding_dataframe["timestamp"][item])
"""

"""def convert_to_prettytime(timestamp):
    time = datetime.strptime(timestamp,"")
    return time"""

