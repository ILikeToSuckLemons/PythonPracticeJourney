import requests
from datetime import datetime

pixela_endpoint = "https://pixe.la/v1/users"
username = "james13"
TOKEN = "jamesgetgit"
userparams = {
    "token": "jamesgetgit",
    "username": "james13",
    "agreeTermsOfService": "yes",
    "notMinor": "yes"
}
# response = requests.post(url=pixela_endpoint, json=userparams)
# print(response.text)

graphendpoint = f"{pixela_endpoint}/{username}/graphs"

graphid = "graph1"
graphconfig = {
    "id": "graph1",
    "name": "Graf",
    "unit": "day",
    "type": "float",
    "color": "sora"
}

header = {
    "X-USER-TOKEN":TOKEN
}
# response = requests.post(url=graphendpoint, json=graphconfig, headers=header)
# print(response.text)
today = datetime(year=2025, month=3, day=24)
print(today.strftime("%Y%m%d"))

graphesendpoint = f"{pixela_endpoint}/{username}/graphs/{graphid}"
graphesconfig = {
    "date": today.strftime("%Y%m%d"),
    "quantity": "15.0"
}

updateendpoint = f"{pixela_endpoint}/{username}/graphs/{graphid}/{today.strftime("%Y%m%d")}"
updateconfig = {
    "quantity": "0.0"
}


deleteendpoint = f"{pixela_endpoint}/{username}/graphs/{graphid}/{today.strftime("%Y%m%d")}"

response = requests.put(url=deleteendpoint, headers=header)
print(response.text)

