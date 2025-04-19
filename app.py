from flask import Flask, render_template, request
import requests
from datetime import datetime, timedelta

app = Flask(__name__)

# Clé API OpenWeatherMap
API_KEY = 'e3244619b4c401aba0b650357b9b8310'  # Remplace par ta clé API

@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        city = request.form['city']
        url = f'http://api.openweathermap.org/data/2.5/weather?q={city}&appid={API_KEY}&units=metric'
        response = requests.get(url)
        data = response.json()
        print(data)  # Affiche les données de l'API dans la console pour déboguer

        if data.get('cod') != 200:
            return render_template('index.html', error="Ville non trouvée")

        # Calcul de l'heure locale
        timezone_offset = data['timezone']  # En secondes
        local_time = datetime.utcfromtimestamp(data['dt'] + timezone_offset).strftime('%H:%M:%S')

        # Récupération des données météo
        weather_data = {
            'city': data['name'],
            'temperature': data['main']['temp'],
            'description': data['weather'][0]['description'].capitalize(),
            'icon': data['weather'][0]['icon'],
            'country': data['sys']['country'],
            'humidity': data['main']['humidity'],
            'wind_speed': data['wind']['speed'],
            'local_time': local_time,
            'lat': data['coord']['lat'],  # Latitude
            'lon': data['coord']['lon']   # Longitude
        }

        return render_template('index.html', weather=weather_data)

    return render_template('index.html')


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=True)
