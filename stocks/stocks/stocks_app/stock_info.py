import finnhub, time
import pandas as pd

def finnhubClient():
    return finnhub.Client(api_key="caq8suiad3iecj6adq7g")

def historicalData(symbol):
    return finnhubClient().stock_candles(symbol.upper(),"D",int(time.time())-4000000,int(time.time()))

def get_last_data(symbol):
    return pd.DataFrame(historicalData(symbol)).drop('s', axis=1).tail(1).to_dict(orient='records')[0]

def get_all_data(symbol):
    return historicalData(symbol)
