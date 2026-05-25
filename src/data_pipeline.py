import ccxt 
import os
import pandas as pd
import time
from sqlalchemy import engine, text
from dotenv import load_dotenv

### environment

load_dotenv()

CRYPTOQUANT = os.getenv("CRYPTO_QUANT")

### paths

BASE_DIR        = os.path.dirname(os.path.abspath(__file__))
DATA_DIR        = os.path.join(BASE_DIR, '..', 'data')
 
RAW_PRICE_DIR   = os.path.join(DATA_DIR, 'raw', 'price')
RAW_ONCHAIN_DIR = os.path.join(DATA_DIR, 'raw', 'onchain')
RAW_SENT_DIR    = os.path.join(DATA_DIR, 'raw', 'sentiment')
RAW_POLY_DIR    = os.path.join(DATA_DIR, 'raw', 'polymarket')
PROCESSED_DIR   = os.path.join(DATA_DIR, 'processed')
 
DB_PATH         = os.path.join(PROCESSED_DIR, 'strategy.db')

# if dont exist then create

for path in [RAW_PRICE_DIR, RAW_ONCHAIN_DIR, RAW_SENT_DIR, RAW_POLY_DIR, PROCESSED_DIR]:
    os.makedirs(path, exist_ok=True)


### parquet helpers

def parquet_exists(path: str):
    return os.path.exists(path)

def save_parquet(df: pd.DataFrame, path: str):
    df.to_parquet(path, index=False)
    print(f'saved → {path}')

def load_parquet(path: str):
    return pd.read_parquet(path)



### ohclv from ccxt

#init exchange
exchange = ccxt.binance({
    'enableRateLimit': True,
})

symbol = 'BTC/USDT'
timeframe = '1d'






