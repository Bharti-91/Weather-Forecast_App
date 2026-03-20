from flask import Flask, render_template, request, jsonify
import requests

import mysql.connector

db= mysql.connector.connect(
        host = "localhost",
        user ="root",
        password ="Admin@12_3",
        database= "weather_app"
    )

cursor = db.cursor()

app = Flask(__name__)

API_KEY = "ce55d11db82a4643f466646f74edd6c3"

@app.route("/")
def home():
    return render_template("index.html")

@app.route("/get_weather")
def get_weather():
    city = request.args.get("city")

    url = f"https://api.openweathermap.org/data/2.5/weather?q={city}&appid={API_KEY}&units=metric"

    response = requests.get(url)
    data = response.json()

    temperature = data['main']['temp']
    humidity = data['main']['humidity']
    weather = data['weather'][0]['description']

    sql = "INSERT INTO weather_data (city, temperature, humidity, weather) VALUES (%s, %s, %s, %s)"
    values = (city, temperature, humidity, weather)
    cursor.execute(sql, values)
    db.commit()
    return jsonify(data)

if __name__ == "__main__":
    app.run(debug=True)

    