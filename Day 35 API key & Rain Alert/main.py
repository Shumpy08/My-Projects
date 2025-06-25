import requests

from twilio.rest import Client

api = "https://api.openweathermap.org/data/2.5/forecast"
api_key = "59f291d921942c20a17bc738c88f1d10"
account_sid = "ACb763b94e0b2db1f83c7e517e21ff4275"
auth_token = "294e5d8c8d61619b3a8d1d661c574692"

parameters = {
    "lat": 12.971599,
    "lon": 77.594566,
    "cnt": 4,
    "appid": api_key
}
response = requests.get(url=api, params=parameters)
response.raise_for_status()
data = response.json()

will_rain = False

for hour_data in data["list"]:
    weather_condition = hour_data["weather"][0]['id']
    if int(weather_condition) < 700:
        will_rain = True

if will_rain:
    client = Client(account_sid, auth_token)
    message = client.messages.create(
        body="Its gonna rain today. Bring an Umbrella ",
        from_="+15162593601",
        to="+917781950588"
    )

    print(message.sid)
else:
    client = Client(account_sid, auth_token)
    message = client.messages.create(
        body='The weather is clear today. No signs of rain. ',
        from_="+15162593601",
        to="+917781950588"
    )
