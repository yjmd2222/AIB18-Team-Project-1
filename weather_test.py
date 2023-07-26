import matplotlib.pyplot as plt
import pandas as pd

df = pd.read_csv('weather_DB.csv')

def load_weather_data(selected_date):
    # Filter the DataFrame to get the weather data for the selected date
    selected_data = df[df['Day'] == selected_date]

    if selected_data.empty:
        print(f"No weather data found for selected date: {selected_date}")
        return None

    return selected_data



def main():
    selected_dates = []

    while True:
        # Get user input for the start date
        start_date = input("Enter the start date (1 to 31) to load weather data (or type 'done' to finish): ")

        # Check if the user wants to stop entering dates
        if start_date.lower() == 'done':
            break

        # Convert the input to an integer (if possible)
        try:
            start_date = int(start_date)
        except ValueError:
            print("Invalid input. Please enter a valid date (1 to 31) or type 'done' to finish.")
            continue

        # Check if the selected date is within the valid range (1 to 31)
        if start_date < 1 or start_date > 31:
            print("Invalid date. Please enter a date between 1 and 31.")
            continue

        # Get user input for the end date
        end_date = input("Enter the end date (1 to 31) to load weather data: ")

        # Convert the input to an integer (if possible)
        try:
            end_date = int(end_date)
        except ValueError:
            print("Invalid input. Please enter a valid date (1 to 31) or type 'done' to finish.")
            continue

        # Check if the selected end date is within the valid range (1 to 31)
        if end_date < 1 or end_date > 31:
            print("Invalid date. Please enter a date between 1 and 31.")
            continue

        # Check if the end date is greater than or equal to the start date
        if end_date < start_date:
            print("End date should be greater than or equal to the start date.")
            continue

        # Generate the list of selected dates within the date range
        selected_dates.extend(range(start_date, end_date + 1))

    # Load weather data for the selected dates
    for date in selected_dates:
        weather_data_for_selected_date = load_weather_data(date)
        if weather_data_for_selected_date is not None:
            print(f"Weather data for selected date ({date}):")
            print(weather_data_for_selected_date.to_string(index=False))  # Print without index number
        print("-" * 80)

if __name__ == "__main__":
    main()
