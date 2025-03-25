import requests

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
response = requests.post(url=graphendpoint, json=graphconfig, headers=header)
print(response.text)