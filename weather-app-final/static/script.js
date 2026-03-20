function getWeather() {

let city = document.getElementById("city").value;

fetch(`/get_weather?city=${city}`)
.then(response => response.json())
.then(data => {

    document.getElementById("cityName").innerText = data.name;

    document.getElementById("temperature").innerText = data.main.temp + "°C";
    document.getElementById("description").innerText = data.weather[0].description;

    let icon = data.weather[0].icon;

    document.getElementById("weatherIcon").src = "https://openweathermap.org/img/wn/" + icon
    +"@2x.png";
    aq
    });
    }

