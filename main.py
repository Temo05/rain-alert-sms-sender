import requests
import os
from twilio.rest import Client

# Read environment variables (works locally if you have .env or in Actions via secrets)
API_KEY = os.getenv("WEATHER_API_KEY")
account_sid = os.getenv("TWILIO_ACCOUNT_SID")
auth_token = os.getenv("TWILIO_AUTH_TOKEN")

parameters = {
    "lat": 46.2767,
    "lon": 41.8268,
    "appid": API_KEY,
    "cnt": 4
}

res = requests.get(url="https://api.openweathermap.org/data/2.5/forecast", params=parameters)
res.raise_for_status()
data = res.json()

will_rain = any(item["weather"][0]["id"] < 700 for item in data["list"])

if will_rain:
    client = Client(account_sid, auth_token)
    message = client.messages.create(
        body="It's going to rain, Bring an umbrella ☔",
        from_='whatsapp:+14155238886',
        to='whatsapp:+995599141205'
    )
    print(message.body)
