# from flask import Flask, render_template, request
# import pandas as pd

# app = Flask(__name__)

# # Read the weather data CSV file
# df = pd.read_csv('weather_DB.csv')

# @app.route('/', methods=['GET', 'POST'])
# def index():
#     if request.method == 'POST':
#         start_date = int(request.form['start_date'])
#         end_date = int(request.form['end_date'])

#         # Filter the DataFrame to get the weather data for the selected date range
#         selected_data = df[(df['Day'] >= start_date) & (df['Day'] <= end_date)]

#         if selected_data.empty:
#             return render_template('app_test.html')

#         # Convert the DataFrame to an HTML table
#         table_html = selected_data.to_html(index=False, classes='table table-striped')

#         return render_template('app_test.html', table_html=table_html)
    
#     return render_template('app_test.html')

# if __name__ == "__main__":
#     app.run(debug=True)



from flask import Flask, render_template, request
import subprocess
import pandas as pd

app = Flask(__name__)

# Load the restaurant data from the CSV file
df = pd.read_csv('weather_DB.csv')

@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        # Get the selected date from the form
        selected_date = request.form['selected_date']

        # Filter the restaurant data for the selected date
        selected_data = df[df['< Date >'] == selected_date]

        # Convert the filtered data to a list of dictionaries
        restaurant_data = selected_data.to_dict(orient='records')

        # Pass the restaurant data to the template for rendering
        return render_template('result.html', date=selected_date, restaurants=restaurant_data)

    return render_template('index2.html', weather_data= weather_data)

def execute_ex_script():
    command = ['python', 'weather_test.py']
    result = subprocess.run(command, capture_output=True, text=True)
    return result.stdout
if __name__ == '__main__':
    app.run(debug=True)
