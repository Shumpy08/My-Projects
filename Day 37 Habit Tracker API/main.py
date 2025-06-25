import requests
import datetime
username = "#"
token = "$"
pixela_endpoint = "https://pixe.la/v1/users"
user_params = {
    "token": "##",
    "username": "$",
    "agreeTermsOfService": "yes",
    "notMinor": "yes"

}
# response = requests.post(pixela_endpoint, json=user_params)
# print(response.text)
graph_endpoint = f"{pixela_endpoint}/{username}/graphs"
headers = {
    "X-USER-TOKEN": token
}
graph_params = {
    "id": "graph2",
    "name": "Workout",
    "unit": "hour",
    "type": "float",
    "color": "ajisai"
}
# response = requests.post(url=graph_endpoint, json=graph_params, headers=headers)
# print(response.text)
today = datetime.datetime.now()
today = today.strftime("%Y%m%d")
print(today)
pixel_params = {
    "date": f"{today}",
    "quantity": input("How many hours did you workout today? "),
}
pixels_endpoint = f"{graph_endpoint}/graph2"
response = requests.post(url=pixels_endpoint, json=pixel_params, headers=headers)
print(response.text)
update_endpoint = f"{pixels_endpoint}/{today}"
update_params = {
    "quantity": "2.5"
}
# response = requests.put(url=update_endpoint, json=update_params, headers=headers)
# print(response.text)
# response = requests.delete(url=update_endpoint, headers=headers)