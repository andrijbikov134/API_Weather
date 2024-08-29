from flask import Flask, request, jsonify, render_template
import requests
import time

app = Flask(__name__)

api_key = "dab2647b113b40fc264d2352a1a9a715"
cities = ["Kyiv", "Khmelnytskyi"]
#local_url = 'http://localhost:5000/update'

weather_data = {
    "weather": "Error",
    "temperature": 0.0,
    "pressure": 0}

def get_weather(c):
    weather_url = f"http://api.openweathermap.org/data/2.5/weather?q={c}&appid={api_key}"
    response = requests.get(weather_url)
    data = response.json()
    weather_data['weather'] = data['weather'][0]['description']
    weather_data['temperature'] = round(float(data['main']['temp']) - 273.15, 1)
    weather_data['pressure'] = data['main']['pressure']
    # Add logic to update other weather data if needed
    return jsonify(weather_data), 200

@app.route('/Kyiv_weather', methods=['GET'])
def kyiv_weather():
    return get_weather(cities[0])

@app.route('/Khmelnytskyi_weather', methods=['GET'])
def khmelnytskyi_weather():
    return get_weather(cities[1])

#@app.route('/')
#def index():
#    return render_template('index.html')

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=5000)

