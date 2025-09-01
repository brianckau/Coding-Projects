#VAR (Value-at-Risk Input Model)
import yfinance as yf
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

ticker = input("Enter the ticker: ")
data = yf.Ticker(ticker).history(period = "5Y", interval = "1D").Close.pct_change().dropna()

c_level = 1 - float(input("Enter the confidence level (in %): "))/100

var = np.percentile(data, c_level)
print(f'\nThe Value-at-Risk is {round(var*100,2)}.')

