import requests

url = "https://api.open-meteo.com/v1/forecast?latitude=23.26&longitude=77.41&current=temperature_2m,relative_humidity_2m"

response = requests.get(url)

print(response.status_code)

weather = response.json()

tem = weather["current"]["temperature_2m"]
print(f"tempreature:{tem}°C")

hum = weather["current"]["relative_humidity_2m"]
print(f"humidity:{hum}%")