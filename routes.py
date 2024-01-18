from app import app
from flask import request, jsonify
from weather import get_weather_by_zip

@app.route('/')
def index():
    return "Welcome to my portfolio backend app!"

@app.route('/wakeup')
def wakeup():
    return 'Backend active', 200

@app.route('/weather', methods=['GET'])
def fetch_weather():
    zip_code = request.args.get('zip', default=None, type=str)
    if not zip_code:
        return jsonify({"error": "Zip code not provided"}), 400
    
    try:
        weather_data = get_weather_by_zip(zip_code)
        recommendation = interpret_weather(weather_data)
        result = {
            "recommendation": recommendation,
            "temperature": weather_data['main']['temp'] - 273.15,
            "weather_condition": weather_data['weather'][0]['main'],
            "wind_speed": weather_data['wind']['speed']
        }
        return jsonify(result)
    except Exception as e:
        return jsonify({"error": str(e)}), 500


    
def interpret_weather(data):
    result = {}

    try:
        result['temperature'] = (data['main']['temp'] - 273.15) * 9/5 + 32
        result['weather_condition'] = data['weather'][0]['main']
        result['weather_description'] = data['weather'][0]['description']
        result['wind_speed'] = data['wind']['speed']
        result['cloud_coverage'] = data['clouds']['all']
        result['visibility'] = data['visibility']
        result['location_name'] = data['name']

    except KeyError:
        result['error'] = "We couldn't retrieve complete weather data, please try entering a valid ZipCode in the United States"
        return result

    if result['temperature'] > 68:
        recommendation = "It's nice outside. Take your dog for a long walk!"
    elif result['weather_condition'] == "Rain":
        recommendation = "Don't walk your dog right now. It's rainy outside, maybe work on one of your apps until it clears up."
    else:
        recommendation = "Go ahead and walk your dog! However, it's a bit cold outside. We recommend that you put on some winter clothes before going out."

    result['recommendation'] = recommendation
    
    return result
