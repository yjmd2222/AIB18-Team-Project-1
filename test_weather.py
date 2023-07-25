import requests
import datetime

from private_info import weather_api_key

def get_weather_in_date_range(api_key, latitude, longitude, start_date, end_date):
    base_url = "http://api.openweathermap.org/data/2.5/forecast"
    params = {
        "lat": latitude,
        "lon": longitude,
        "appid": api_key,
        "units": "metric",  # Use "imperial" for Fahrenheit
    }

    response = requests.get(base_url, params=params)

    if response.status_code == 200:
        weather_data = response.json()
        start_date = datetime.datetime.strptime(start_date, "%Y-%m-%d")
        end_date = datetime.datetime.strptime(end_date, "%Y-%m-%d") + datetime.timedelta(days=1)
        weather_info_by_date = {}

        for item in weather_data["list"]:
            dt = datetime.datetime.fromtimestamp(item["dt"])
            date = dt.date()

            if start_date <= dt < end_date:
                # Check if there is already a weather entry for this date
                if date not in weather_info_by_date:
                    weather_info_by_date[date] = item
                else:
                    # Choose the data point with the closest timestamp to noon (12:00 PM)
                    current_time_difference = abs((weather_info_by_date[date]["dt"] - datetime.datetime.combine(date, datetime.time(12, 0, 0)).timestamp()))
                    new_time_difference = abs((item["dt"] - datetime.datetime.combine(date, datetime.time(12, 0, 0)).timestamp()))

                    if new_time_difference < current_time_difference:
                        weather_info_by_date[date] = item

        # Extract relevant information from the selected data points
        selected_weather_info = []
        for date, item in weather_info_by_date.items():
            day_of_week = datetime.datetime.fromtimestamp(item["dt"]).strftime("%A")
            temperature = item["main"]["temp"]
            weather_description = item["weather"][0]["description"]
            selected_weather_info.append((date, day_of_week, temperature, weather_description))

        return selected_weather_info
    else:
        print("Failed to fetch weather data.")
        return None

# Replace 'YOUR_API_KEY' with your actual OpenWeather API key
api_key = weather_api_key
latitude = 33.4996  # Latitude of Jeju Island
longitude = 126.5312  # Longitude of Jeju Island
start_date = "2023-07-25"  # Replace with your desired start date (format: "YYYY-MM-DD")
end_date = "2023-07-30"    # Replace with your desired end date (format: "YYYY-MM-DD")

weather_data_in_date_range = get_weather_in_date_range(api_key, latitude, longitude, start_date, end_date)

if weather_data_in_date_range:
    print(f"Weather from {start_date} to {end_date}:")
    for date, day_of_week, temp, description in weather_data_in_date_range:
        print(f"{date}: {day_of_week}, Temperature {temp}°C, Description: {description}")
else:
    print("No weather data available.")