from flask import Flask, render_template, request
from heejae_weather import main  # import the main function from 05_weather_dat.py

app = Flask(__name__)

@app.route('/')
def index():
    return '''
        <!DOCTYPE html>
        <html>
        <head>
        <title>제주도 날씨와 맛집</title>
        </head>
        <body>
        <h1>제주도 날씨와 맛집 정보🍊</h1>
        <h2></h2>
        <p>날짜를 입력해주세요🗓️</p>
        <form action="/process" method="post">  <!-- change the action attribute -->
            <h2>
            <label for="start_date">Start Date:</label>
            <input type="date" id="start_date" name="start_date" required>
            <label for="end_date">End Date:</label>
            <input type="date" id="end_date" name="end_date" required>
            </h2>
            <button type="submit">Enter</button>
        </form>
        </body>
        </html>
    '''

@app.route('/process', methods=['POST'])
def process():
    start_date = request.form['start_date']  # Get the value of the 'start_date' input
    end_date = request.form['end_date']  # Get the value of the 'end_date' input
    output = main(start_date, end_date)  # Call the main function from 05.py with the start_date and end_date
    
    return render_template('output.html', start_date=start_date, end_date=end_date, output=output)
    
if __name__ == '__main__':
    app.run()


from flask import Flask, render_template, request
import subprocess

app = Flask(__name__)

@app.route('/')
def index():
    return '''
        <!DOCTYPE html>
        <html>
        <head>
            <title>Our Company</title>
        </head>
        <body>
            <h1>제주도 날씨와 맛집🍊</h1>
            <h2></h2>
            <p>↓위치를 입력해주세요 ↓  </p>
            <form action="/process" method="post">
                <h2>
                    <input type="text" name="location" 위치="위치" placeholder="현재 위치">
                </h2>
                <button type="submit">입력 (●'ᴗ'●)ﾉ♥</button>
            </form>
        </body>
        </html>
    '''

# 기존 
# @app.route('/process', methods=['POST'])
# def process():
#     location = request.form['location']  # Get the value of the 'location' input
#     output = execute_ex_script(location)  # Execute ex.py with the location and get the output
    
#     return render_template('output.html', location=location, output=output)

# def execute_ex_script(location):
#     command = ['python', '03_weather_mango.py', location]
#     result = subprocess.run(command, capture_output=True, text=True)
#     return result.stdout

# if __name__ == '__main__':
#     app.run()

# # app.py
# import time
# import pandas as pd
# from flask import Flask, render_template
# from bs4 import BeautifulSoup
# from selenium import webdriver
# from selenium.webdriver.common.by import By
# from selenium.webdriver.chrome.options import Options

# app = Flask(__name__)

# def scrape_restaurant_data(keyword):
#     url = f"https://www.mangoplate.com/search/{keyword}"

#     chrome_options = Options()
#     driver = webdriver.Chrome(options = chrome_options)
#     driver.get(url)

#     req = driver.page_source
#     soup = BeautifulSoup(req, "html.parser")
#     info_list = soup.find_all(name="div", attrs={"class": "info"})

#     # Initialize lists to store data
#     titles = []
#     total_scores = []
#     addresses = []
#     menus = []

#     # ... Extract data from info_list and populate the lists ...

#     driver.quit()  # Quit the web driver

#     # Convert data to a DataFrame
#     data = {
#         'Title': titles,
#         'Total Score': total_scores,
#         'Address': addresses,
#         'Menu': menus
#     }
#     df = pd.DataFrame(data)

#     return df
#     return df



# @app.route('/')
# def index():
#     keyword = 'Jeju Island'
#     restaurant_data = scrape_restaurant_data(keyword)
#     #weather_data = get_weather_data()
#     return render_template('index.html', restaurant_data=restaurant_data) #, weather_data=weather_data)

# if __name__ == '__main__':
#     app.run(debug=True)
