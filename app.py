from flask import Flask, request
import requests
import logging
from datetime import datetime

app = Flask(__name__)

AUTHOR = "Julia Stanczak"
PORT = 8080

logging.basicConfig(level=logging.INFO)
logging.info(f"Data uruchomienia: {datetime.now()}")
logging.info(f"Autor: {AUTHOR}")
logging.info(f"Aplikacja nasłuchuje na porcie TCP: {PORT}")

LOCATIONS = {
    "Polska": {
        "Lublin": (51.2465, 22.5684),
        "Warszawa": (52.2297, 21.0122),
        "Kraków": (50.0647, 19.9450)
    },
    "Niemcy": {
        "Berlin": (52.5200, 13.4050),
        "Monachium": (48.1351, 11.5820)
    }
}

@app.route("/", methods=["GET", "POST"])
def index():
    weather = ""

    if request.method == "POST":
        country = request.form.get("country")
        city = request.form.get("city")
        lat, lon = LOCATIONS[country][city]

        url = (
            f"https://api.open-meteo.com/v1/forecast"
            f"?latitude={lat}&longitude={lon}&current_weather=true"
        )

        response = requests.get(url)
        data = response.json()
        current = data["current_weather"]

        weather = f"""
        <h2>Pogoda dla: {city}, {country}</h2>
        <p>Temperatura: {current['temperature']} °C</p>
        <p>Prędkość wiatru: {current['windspeed']} km/h</p>
        <p>Kierunek wiatru: {current['winddirection']}°</p>
        """

    return f"""
    <html>
    <head>
        <title>Aplikacja pogodowa</title>
    </head>
    <body>
        <h1>Aplikacja pogodowa</h1>

        <form method="POST">
            <label>Kraj:</label>
            <select name="country">
                <option value="Polska">Polska</option>
                <option value="Niemcy">Niemcy</option>
            </select>

            <br><br>

            <label>Miasto:</label>
            <select name="city">
                <option value="Lublin">Lublin</option>
                <option value="Warszawa">Warszawa</option>
                <option value="Kraków">Kraków</option>
                <option value="Berlin">Berlin</option>
                <option value="Monachium">Monachium</option>
            </select>

            <br><br>

            <button type="submit">Pokaż pogodę</button>
        </form>

        {weather}
    </body>
    </html>
    """

@app.route("/health")
def health():
    return "OK", 200

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=PORT)