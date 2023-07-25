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

@app.route('/process', methods=['POST'])
def process():
    location = request.form['location']  # Get the value of the 'location' input
    output = execute_ex_script(location)  # Execute ex.py with the location and get the output
    
    return render_template('output.html', location=location, output=output)

def execute_ex_script(location):
    command = ['python', '03_weather_mango.py', location]
    result = subprocess.run(command, capture_output=True, text=True)
    return result.stdout

if __name__ == '__main__':
    app.run()
