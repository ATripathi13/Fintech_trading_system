import pandas as pd

def run_strategy():
    df = pd.read_csv('data/stock_data.csv')
    df['SMA_50'] = df['price'].rolling(window=50).mean()
    df['SMA_200'] = df['price'].rolling(window=200).mean()

    df['signal'] = 0
    df.loc[df['SMA_50'] > df['SMA_200'], 'signal'] = 1
    df.loc[df['SMA_50'] < df['SMA_200'], 'signal'] = -1

    trades = df[df['signal'].diff() != 0][['date', 'price', 'signal']]
    # Convert signal: 1=Buy, -1=Sell
    trades['signal'] = trades['signal'].map({1: 'Buy', -1: 'Sell'})

    total_profit_loss = 0  # Placeholder: add logic if you want P/L calculation here

    return {
        "trades": trades.to_dict(orient='records'),
        "total_profit_loss": total_profit_loss
    }
