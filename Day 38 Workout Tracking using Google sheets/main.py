import requests
from datetime import datetime
import os
url = "https://trackapi.nutritionix.com/v2/natural/exercise"
sheety_api = (
    "https://api.sheety.co/5578977c2f83834148ce4c60bd1fa87d/"
    "copyOfMyWorkouts/workouts"
)

AGE = 18
WEIGHT = 78
HEIGHT = 177
GENDER = "male"
API_ID = os.environ["API_ID"]
API_KEY = os.environ["API_KEY"]
print(API_ID)
print(API_KEY)
now_time = datetime.now().strftime("%X")
now_date = datetime.now().strftime("%d-%m-%Y")


QUERY = input("What exercises did you do today: ")

headers = {
    "x-app-id": API_ID,
    "x-app-key": API_KEY
}
params = {
    "query": QUERY,
    "gender": GENDER,
    "weight_kg": WEIGHT,
    "height_cm": HEIGHT,
    "age": AGE
}

response = requests.post(url=url, json=params, headers=headers)
response.raise_for_status()
data = response.json()

bearer_headers = {
    "Authorization": "Bearer YOUR_TOKEN"
}
for exercise in data["exercises"]:
    sheet_inputs = {
        "workout": {
            "date": now_date,
            "time": now_time,
            "exercise": exercise["name"].title(),
            "duration": exercise["duration_min"],
            "calories": exercise["nf_calories"]
        }
    }
    sheet_response = requests.post(url=sheety_api, json=sheet_inputs, headers=bearer_headers)

    print(sheet_response.text)
