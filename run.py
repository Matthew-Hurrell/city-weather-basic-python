import requests

API_KEY = "4cc9c46d7c87a9eebb5f478d2a3f415b"
BASE_URL = "http://api.openweathermap.org/data/2.5/weather"

city = input("Enter a city name: ")
request_url = f"{BASE_URL}?appid={API_KEY}&q={city}"
response = requests.get(request_url)

if response.status_code == 200:
    data = response.json()
    weather = data['weather'][0]["description"]
    print("Weather:", weather.capitalize())
    temperature = round(data["main"]["temp"] - 273.15, 2)
    print("Temperature:", temperature, "celcius")
else:
    print("An error occurred.")