from flask import Flask, request, jsonify, render_template
import requests
import time

app = Flask(__name__)

api_key = "dab2647b113b40fc264d2352a1a9a715"
city = "Kyiv"
weather_url = f"http://api.openweathermap.org/data/2.5/weather?q={city}&appid={api_key}"
local_url = 'http://localhost:5000/update'

weather_data = {
    "weather": "Error",
    "temperature": 0.0,
    "pressure": 0}

@app.route('/current_weather', methods=['GET'])
def get_weather():
    global weather_data
    response = requests.get(weather_url)
    data = response.json()
    weather_data['weather'] = data['weather'][0]['description']
    weather_data['temperature'] = round(float(data['main']['temp']) - 273.15, 1)
    weather_data['pressure'] = data['main']['pressure']
    # Add logic to update other weather data if needed
    return jsonify(weather_data), 200

@app.route('/')
def index():
    return render_template('index.html')

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=5000)

