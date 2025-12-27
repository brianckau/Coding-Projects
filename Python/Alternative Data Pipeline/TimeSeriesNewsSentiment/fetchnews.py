import pandas as pd
import numpy as np
from pygooglenews import GoogleNews
from transformers import pipeline

def fetch_google_news(query:str, start_date:str, end_date:str):

    news = GoogleNews(lang='en',country='US')

    max_length = 0

    df = pd.DataFrame()

    for day in pd.date_range(start_date,end_date,freq='D'):
        length = len(news.search(query,when=day.strftime("%Y-%m-%d")).get("entries",[]))
        if length > max_length:
            max_length = length
        
    for day in pd.date_range(start_date,end_date,freq='D'):
        df[f'{day.year}-{day.month}-{day.day}'] = [np.nan for x in range(max_length)]

    for day in pd.date_range(start_date,end_date,freq='D'):
        entries = news.search(query, when=day.strftime("%Y-%m-%d")).get("entries",[])
        titles = [e.get("title") for e in entries]
        df.loc[:len(titles)-1,f'{day.year}-{day.month}-{day.day}'] = titles
    return df

def sentiment_analysis(query: str, start_date: str, end_date: str, mode):
    classifier = pipeline("sentiment-analysis")

    df = fetch_google_news(query, start_date, end_date)

    for col in df.columns:
        outcol = f"{col} Analysis"
        df.loc[:,outcol] = np.nan

        for row in range(len(df)):
            text = df.loc[row, col]
            if pd.isna(text):
                continue
            if mode == "score":
                df.loc[row, outcol] = classifier(str(text))[0]["score"]
            elif mode == "label":
                df.loc[row, outcol] = classifier(str(text))[0]["label"]
    return df

