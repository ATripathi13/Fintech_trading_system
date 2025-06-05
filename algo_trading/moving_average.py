import pandas as pd

df = pd.read_csv('data/stock_data.csv')
df['SMA_50'] = df['price'].rolling(window=50).mean()
df['SMA_200'] = df['price'].rolling(window=200).mean()

df['signal'] = 0
df.loc[df['SMA_50'] > df['SMA_200'], 'signal'] = 1
df.loc[df['SMA_50'] < df['SMA_200'], 'signal'] = -1

# Generate buy/sell signals
trades = df[df['signal'].diff() != 0][['date', 'price', 'signal']]
print(trades)
