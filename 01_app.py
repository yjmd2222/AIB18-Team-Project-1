# # # from flask import Flask, render_template, request
# # # from heejae_weather import main  # import the main function from 05_weather_data.py
# # # import time
# # # from selenium import webdriver
# # # from selenium.webdriver.common.by import By
# # # import pandas as pd
# # # from bs4 import BeautifulSoup
# # # import subprocess

# # # app = Flask(__name__)

# # # @app.route('/')
# # # def index():
# # #     return '''
# # #         <!DOCTYPE html>
# # #         <html>
# # #         <head>
# # #         <title>Our Company</title>
# # #         </head>
# # #         <body>
# # #         <h1>Jeju Island weather and restaurants</h1>
# # #         <h2></h2>
# # #         <p>Enter the dates:</p>
# # #         <form action="/process" method="post">  <!-- change the action attribute -->
# # #             <h2>
# # #             <label for="start_date">Start Date:</label>
# # #             <input type="date" id="start_date" name="start_date" required>
# # #             <label for="end_date">End Date:</label>
# # #             <input type="date" id="end_date" name="end_date" required>
# # #             </h2>
# # #             <button type="submit">Enter</button>
# # #         </form>
# # #         </body>
# # #         </html>
# # #     '''

# # # @app.route('/process', methods=['POST'])
# # # def execute_ex_script():
# # #     command = ['python', '02_mangoplate.py']
# # #     result = subprocess.run(command, capture_output=True, text=True)

# # #     return result.stdout

# # # def process():
# # #     start_date = request.form['start_date']  # Get the value of the 'start_date' input
# # #     end_date = request.form['end_date']  # Get the value of the 'end_date' input
    
   
# # #     output = main(start_date, end_date)  # Call the main function from 05.py with the start_date and end_date
# # #     weather_and_restaurant_data = execute_ex_script(location="제주도")
# # #     weather_output, restaurant_output = weather_and_restaurant_data.split("\n", 1)

# # #     # Render the output.html template and pass the weather and restaurant data to it
# # #     return render_template('output.html', start_date=start_date, end_date=end_date, weather_output=weather_output, restaurant_output=restaurant_output)


    
# # #     location = request.form['location']  # Get the value of the 'location' input
# # #     output = execute_ex_script(location)  # Execute ex.py with the location and get the output
    
# # #     return render_template('output.html', location=location, output=output)

# # # def execute_ex_script(location):
# # #     command = ['python', '03_weather_mango.py', location]
# # #     result = subprocess.run(command, capture_output=True, text=True)
# # #     return result.stdout


# # from flask import Flask, render_template, request
# # from heejae_weather import main  # import the main function from 05_weather_data.py
# # import time
# # from selenium import webdriver
# # from selenium.webdriver.common.by import By
# # import pandas as pd
# # from bs4 import BeautifulSoup
# # import subprocess

# # app = Flask(__name__)

# # @app.route('/')
# # def index():
# #     return '''
# #         <!DOCTYPE html>
# #         <html>
# #         <head>
# #         <title>Our Company</title>
# #         </head>
# #         <body>
# #         <h1>Jeju Island weather and restaurants</h1>
# #         <h2></h2>
# #         <p>Enter the dates:</p>
# #         <form action="/process" method="post">  <!-- change the action attribute -->
# #             <h2>
# #             <label for="start_date">Start Date:</label>
# #             <input type="date" id="start_date" name="start_date" required>
# #             <label for="end_date">End Date:</label>
# #             <input type="date" id="end_date" name="end_date" required>
# #             </h2>
# #             <button type="submit">Enter</button>
# #         </form>
# #         </body>
# #         </html>
# #     '''

# # def execute_ex_script(location):
# #     command = ['python', '02_mangoplate.py']
# #     result = subprocess.run(command, capture_output=True, text=True)
# #     return result.stdout

# # @app.route('/process', methods=['POST'])
# # def process():
# #     start_date = request.form['start_date']  # Get the value of the 'start_date' input
# #     end_date = request.form['end_date']  # Get the value of the 'end_date' input

# #     output = main(start_date, end_date)  # Call the main function from 05.py with the start_date and end_date
# #     weather_and_restaurant_data = execute_ex_script(location="제주도")
# #     weather_output, restaurant_output = weather_and_restaurant_data.split("\n", 1)

# #     # Render the output.html template and pass the weather and restaurant data to it
# #     return render_template('output.html', start_date=start_date, end_date=end_date, weather_output=weather_output, restaurant_output=restaurant_output)

# # if __name__ == '__main__':
# #     app.run()

# from flask import Flask, render_template, request
# from heejae_weather import main  # import the main function from 05_weather_data.py
# import time
# from selenium import webdriver
# from selenium.webdriver.common.by import By
# import pandas as pd
# from bs4 import BeautifulSoup
# import subprocess

# app = Flask(__name__)

# @app.route('/')
# def index():
#     return '''
#         <!DOCTYPE html>
#         <html>
#         <head>
#         <title>Our Company</title>
#         </head>
#         <body>
#         <h1>Jeju Island weather and restaurants</h1>
#         <h2></h2>
#         <p>Enter the dates:</p>
#         <form action="/process" method="post">  <!-- change the action attribute -->
#             <h2>
#             <label for="start_date">Start Date:</label>
#             <input type="date" id="start_date" name="start_date" required>
#             <label for="end_date">End Date:</label>
#             <input type="date" id="end_date" name="end_date" required>
#             </h2>
#             <button type="submit">Enter</button>
#         </form>
#         </body>
#         </html>
#     '''

# def execute_ex_script(location):
#     command = ['python', '02_mangoplate.py']
#     result = subprocess.run(command, capture_output=True, text=True)
#     return result.stdout


# @app.route('/process', methods=['POST'])
# def process():
#     start_date = request.form['start_date']  # Get the value of the 'start_date' input
#     end_date = request.form['end_date']  # Get the value of the 'end_date' input

#     output = main(start_date, end_date)  # Call the main function from 05.py with the start_date and end_date
#     weather_and_restaurant_data = execute_ex_script(location="제주도")
#     weather_output, restaurant_output = weather_and_restaurant_data.split("\n", 1)

#     # Render the output.html template and pass the weather and restaurant data to it
#     return render_template('output.html', start_date=start_date, end_date=end_date, weather_output=weather_output, restaurant_output=restaurant_output)

# if __name__ == '__main__':
#     app.run()


