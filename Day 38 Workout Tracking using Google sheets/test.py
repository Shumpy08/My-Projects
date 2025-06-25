import requests

APP_ID = "#"
API_KEY = "##"
API_ENDPOINT = "https://trackapi.nutritionix.com/v2/natural/exercise"
headers = {
    "x-app-id": APP_ID,
    "x-app-key": API_KEY
}
GENDER = "male"
WEIGHT_KG = 78
HEIGHT_CM = 177
AGE = 18

sentence = input("Tell me which exercise you did? ")
parameters = {
    "query": sentence,
    "gender": GENDER,
    "weight_kg": WEIGHT_KG,
    "height_cm": HEIGHT_CM,
    "age": AGE
}

response = requests.post(url=API_ENDPOINT, json=parameters, headers=headers)
response.raise_for_status()
print(response.json())
