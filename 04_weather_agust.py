import time
from selenium import webdriver
from selenium.webdriver.common.by import By
import pandas as pd
from bs4 import BeautifulSoup
import sys
from tabulate import tabulate
import re

# Initialize the webdriver
driver = webdriver.Chrome()

# Lists to store the weather data
days = []
weathers = []
low_temps = []
high_temps = []

# Define a function to extract weather data for a given URL
def get_weather_data(url, day):
    driver.get(url)
    time.sleep(1)  # Add a delay to ensure the page loads completely

    # Parse the page with BeautifulSoup
    req = driver.page_source
    soup = BeautifulSoup(req, "html.parser")

    # Extract the weather, low temperature, and high temperature
    element = 'div.half-day-card-content > div.phrase'
    weather_element = driver.find_element(By.CSS_SELECTOR, element)
    weather = weather_element.text
    weathers.append(weather)

    element = 'div.half-day-card-header > div.half-day-card-header__content > div.weather > div'
    high_temp_element = driver.find_element(By.CSS_SELECTOR, element)
    high_temp = high_temp_element.text
    high_temps.append(high_temp)

    element = 'div:nth-child(4) > div.half-day-card-header > div.half-day-card-header__content > div.weather > div'
    low_temp_element = driver.find_element(By.CSS_SELECTOR, element)
    low_temp = low_temp_element.text
    low_temps.append(low_temp)
    
    # Append the adjusted day to the days list
    adjusted_day = day - 6
    days.append(adjusted_day)

# Loop through different URLs
for day in range(7, 38):
    url = f"https://www.accuweather.com/ko/kr/jeju/224209/daily-weather-forecast/224209?day={day}"
    get_weather_data(url, day)

# Close the webdriver
driver.quit()

# Create a dataframe using the collected data
weather_df = pd.DataFrame({
    'Day': days,
    'Weather': weathers,
    'Low Temperature': low_temps,
    'High Temperature': high_temps
})

def extract_numeric_value(text):
    match = re.search(r'\d+', text)
    return int(match.group()) if match else None

# Apply the function to the "Low Temperature" and "High Temperature" columns
weather_df['Low Temperature'] = weather_df['Low Temperature'].apply(extract_numeric_value)
weather_df['High Temperature'] = weather_df['High Temperature'].apply(extract_numeric_value)


# Print the dataframe using tabulate
print(tabulate(weather_df, headers='keys', tablefmt='plain', showindex=False, numalign='center'))

file_name = 'weather_DB.csv'
weather_df.to_csv(file_name, index=False, encoding='utf-8-sig') 

