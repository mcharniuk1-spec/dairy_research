import requests
import pandas as pd
import io

url = "https://data-api.ecb.europa.eu/service/data/EXR/D.UAH.EUR.SP00.A?format=csvdata"

response = requests.get(url)

csv_data = response.content.decode('utf-8')

df = pd.read_csv(io.StringIO(csv_data))

# ECB structure uses TIME_PERIOD column
df['date'] = pd.to_datetime(df['TIME_PERIOD'])

# ECB gives UAH per EUR already
df = df[['date', 'OBS_VALUE']]
df.columns = ['date', 'EUR_UAH']

# Filter period
df = df[df['date'] >= '2021-12-01']

# Sort
df = df.sort_values('date')

# Save
df.to_excel("EUR_UAH_daily_ECB.xlsx", index=False)

print("Saved:", len(df), "rows")
