import requests

BASE_URL = "https://api.openweathermap.org/data/2.5/weather"
API_KEY = "03fbbc7516b46760a3c78ebdd870c765"

city = input("Enter the City: ")

request_url = f"{BASE_URL}?appid={API_KEY}&q={city}"

print(request_url)

response = requests.get(request_url)

if response.status_code == 200:
    data = response.json()
    weather = data['weather'][0]['description']
    print(f"Weather: {weather}")
    temprature = round((data['main']['temp'] - 273.15), 2)
    print(f"{temprature}C")

else:
    print("City Not Found!")
