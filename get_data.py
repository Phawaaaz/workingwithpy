import requests 
from datetime import datetime, timedelta
import pandas as pd
import matplotlib.pyplot as plt
import csv



# Calculate dates 
today = datetime.now()

week_ago = today - timedelta(days=7)

# Format dates as strings
start_date = week_ago.strftime('%Y-%m-%d')
end_date = today.strftime('%Y-%m-%d')

# API endpoint and parameters
url = f"https://api.open-meteo.com/v1/forecast?latitude=6.6137&longitude=3.3553&start_date={start_date}&end_date={end_date}&daily=temperature_2m_max,temperature_2m_min"

# Make the API request
response = requests.get(url)

if response.status_code == 200:
    data = response.json()
    print(data)
else:    print(f"Error fetching data: {response.status_code}")


# ---------------------------------------------


# Extract the daily data
daily_data = data['daily']

# Create a DataFrame
df = pd.DataFrame({
    'date': daily_data['time'],
    'max_temp': daily_data['temperature_2m_max'],
    'min_temp': daily_data['temperature_2m_min']
})

# Convert date strings to datetime
df['date'] = pd.to_datetime(df['date'])

print(df)


# Create the plot
plt.figure(figsize=(10, 6))
plt.plot(df['date'], df['max_temp'], marker='o', label='Max Temp')
plt.plot(df['date'], df['min_temp'], marker='o', label='Min Temp')

# Add labels and title
plt.xlabel('Date')
plt.ylabel('Temperature (°C)')
plt.title('Lagos Weather - Past 7 Days')
plt.legend()

# Rotate x-axis labels for readability
plt.xticks(rotation=45)
plt.tight_layout()

# Save the plot
plt.savefig('weather_chart.png')
plt.show()

def save_data_to_csv(df, filename='weather_data.csv'):
    df.to_csv(filename , index=False)
    print(f"Data saved to {filename}")
    
save_data_to_csv(df)

