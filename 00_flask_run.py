from flask import Flask, render_template, request
import subprocess

import flask_1p_option_selection

app = Flask(__name__)
app.register_blueprint(flask_1p_option_selection.bp)

@app.route('/')
def index():
    return '''
        <!DOCTYPE html>
        <html>
        <head>
            <title>Our Company</title>
        </head>
        <body>
            <h1>제주도 날씨와 맛집</h1>
            <h2></h2>
            <p>위치를 입력해주세요</p>
            <form action="/process" method="post">
                <h2>
                    <input type="text" name="location" 위치="위치" placeholder="현재 위치">
                </h2>
                <button type="submit">입력</button>
            </form>
        </body>
        </html>
    '''

@app.route('/process', methods=['POST'])
def process():
    location = request.form['location']  
    output = execute_ex_script(location)  
    
    return render_template('output.html', location=location, output=output)


def execute_ex_script(location):
    command = ['python', '03_weather_mango.py', location]
    result = subprocess.run(command, capture_output=True, text=True)
    return result.stdout

if __name__ == '__main__':
    app.run()