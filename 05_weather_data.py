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
    # Get user input for the start date
    while True:
        start_date = input("Enter the start date (1 to 31): ")
        try:
            start_date = int(start_date)
        except ValueError:
            print("Invalid input. Please enter a valid date (1 to 31).")
            continue

        # Check if the selected date is within the valid range (1 to 31)
        if start_date < 1 or start_date > 31:
            print("Invalid date. Please enter a date between 1 and 31.")
            continue
        break

    # Get user input for the end date
    while True:
        end_date = input("Enter the end date (1 to 31): ")
        try:
            end_date = int(end_date)
        except ValueError:
            print("Invalid input. Please enter a valid date (1 to 31).")
            continue

        # Check if the selected end date is within the valid range (1 to 31)
        if end_date < 1 or end_date > 31:
            print("Invalid date. Please enter a date between 1 and 31.")
            continue
        break

    # Check if the end date is greater than or equal to the start date
    if end_date < start_date:
        print("End date should be greater than or equal to the start date.")
        return

    # Generate the list of selected dates within the date range
    selected_dates = list(range(start_date, end_date + 1))

    # Load weather data for the selected dates
    for date in selected_dates:
        weather_data_for_selected_date = load_weather_data(date)
        if weather_data_for_selected_date is not None:
            print(f" {date}일 날씨")
            print(weather_data_for_selected_date.to_string(index=False, col_space=15, justify='left'))  
        print("-" * 80)

if __name__ == "__main__":
    main()
