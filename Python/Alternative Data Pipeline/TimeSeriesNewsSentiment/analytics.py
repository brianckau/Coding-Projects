import pandas as pd
import numpy as np
from transformers import pipeline
import matplotlib.pyplot as plt
from matplotlib.dates import AutoDateLocator, ConciseDateFormatter
from matplotlib.font_manager import FontProperties
import yfinance as yf

def time_series_sentiment(df,query,sma_days):
    #Plot and return time series
    time_series = pd.Series(dtype="float64")
    

    count = 0

    for col in df.columns:
        if "Analysis" in col:
            time_series.loc[col] = (df[f"{col}"].value_counts()["POSITIVE"]/
                                    (df[f'{col}'].value_counts()["NEGATIVE"]+
                                    df[f"{col}"].value_counts()["POSITIVE"]))

    time_series.index = time_series.index.str.removesuffix(" Analysis")
    
    sma_time_series = time_series.rolling(window=sma_days).mean()
    sma_time_series.index = time_series.index

    fig, ax = plt.subplots(figsize=(15,8))

    ax.plot(time_series,color="blue",alpha=0.9,label=f"{query} News Sentiment",lw=1)
    ax.plot(sma_time_series,color="red",alpha=0.9,label=f"Smoothed {query} News Sentiment, SMA-{sma_days}",lw=1)

    ax.set(title=f"Time-Series Google News Sentiment Plot for {query}",
           xlabel="Date", ylabel="Sentiment Score")
    
    loc = AutoDateLocator()
    ax.xaxis.set_major_locator(loc)
    ax.xaxis.set_major_formatter(ConciseDateFormatter(loc))

    fp = FontProperties(family="Times New Roman",size=12,weight="bold")

    ax.legend(prop=fp)

    return time_series


def sentiment_returns_analysis(series, ticker):

    series = series.copy()
    series.index = pd.to_datetime(series.index)
    if getattr(series.index, "tz", None) is not None:
        series.index = series.index.tz_localize(None)

    stock_data = yf.download(
        tickers=ticker,
        start=pd.to_datetime(series.index[0]),
        end=pd.to_datetime(series.index[-1]),
    )["Close"][f"{ticker}"]

    stock_data = stock_data.copy()
    stock_data.index = pd.to_datetime(stock_data.index)
    if getattr(stock_data.index, "tz", None) is not None:
        stock_data.index = stock_data.index.tz_localize(None)

    sentiment_returns_df = pd.concat([stock_data.rename("stock"), series.rename("sentiment")], axis=1).dropna()

    fig, ax = plt.subplots(figsize=(15, 6))

    ax2 = ax.twinx()

    l1, = ax.plot(series.index, series.values, color="blue", alpha=0.9, lw=1, label="News Sentiment")
    l2, = ax2.plot(stock_data.index, stock_data.values, color="red", alpha=0.9, lw=1, label=f"{ticker} close price")

    ax.set_title(f"{ticker} price & related news sentiment")
    ax.set_xlabel("Date")
    ax.set_ylabel("Sentiment Score")
    ax2.set_ylabel("Asset Price")

    ax.legend(handles=[l1, l2], loc="upper left")
    plt.show()

    print(f'Correlation: {round(sentiment_returns_df['stock'].corr(sentiment_returns_df['sentiment']),4)}')

    return sentiment_returns_df
