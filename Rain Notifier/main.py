import requests
from twilio.rest import Client

api_key = "you_api_key"
latitude = 52.520008
longitude = 13.404954
account_sid = "your_account"
auth_token = "your_token"
client = Client(account_sid, auth_token)
parameters = {
    "lat": latitude,
    "lon": longitude,
    "appid": api_key,
    "exclude": "current,minutely,daily"
}
response = requests.get(url="https://api.openweathermap.org/data/3.0/onecall", params=parameters)
print(response.status_code)
response.raise_for_status()
weather_data = response.json()
print(weather_data)
weather_data_id = []
will_rain = False
for hour_data in weather_data["hourly"][:12]:
    if hour_data["weather"][0]["id"] < 700:
        will_rain = True

if will_rain:
    message = client.messages.create(
        body="Bring your umbrella",
        from_='your twilio nr',
        to='your personal number'
    )

