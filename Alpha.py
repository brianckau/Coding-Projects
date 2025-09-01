import pandas as pd
import requests
from io import StringIO
import matplotlib.pyplot as plt
api = "H7WKQIGFRDPFG4A5"
url = f"https://www.alphavantage.co/query?function=TIME_SERIES_DAILY&symbol=AMZN&&apikey={api}&datatype=csv"

response = requests.get(url)
# Check if the response looks like a CSV with expected columns
if 'timestamp' not in response.text or 'close' not in response.text:
    print("Error: API did not return expected CSV data. Response was:")
    print(response.text)
    exit(1)

data = pd.read_csv(StringIO(response.text))
# Convert timestamp to datetime before plotting
if data['timestamp'].dtype != 'datetime64[ns]':
    data['timestamp'] = pd.to_datetime(data['timestamp'])
data.set_index('timestamp', inplace=True)
mean = data.close.mean()
plt.figure(figsize=(10, 5))
plt.plot(data.index, data['close'], label='Close Price')
plt.axhline(mean, color='red', linestyle='-', label='Mean Close Price')
plt.xlabel('Date')
plt.ylabel('Price')
plt.title('AMZN Daily Close Price with Mean')
plt.xticks(rotation=45)
plt.legend()
plt.tight_layout()
print(f"Mean Close Price: {mean}")
print(data.head())
print(data.tail())
print(data.describe())
print(data.info())
print(data.columns)
print(data.shape)
print(data.isnull().sum())
print(data.dtypes)
plt.show()
