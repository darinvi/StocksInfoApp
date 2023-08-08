import finnhub, time
import pandas as pd

def finnhubClient():
    return finnhub.Client(api_key="caq8suiad3iecj6adq7g")

def historicalData(symbol):
    return pd.DataFrame(finnhubClient().stock_candles(symbol.upper(),"D",int(time.time())-4000000,int(time.time()))).drop('s', axis=1)

def get_last_data(symbol):
    return historicalData(symbol).tail(1).to_dict(orient='records')[0]
