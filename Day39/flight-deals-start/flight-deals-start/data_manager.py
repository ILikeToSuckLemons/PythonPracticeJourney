import requests
class DataManager:
    endpoint = "https://api.sheety.co/f04b0bc0b4cd3207882370dfc0cd0b90/copyOfFlightDeals/prices"
    response = requests.get(endpoint)
    #This class is responsible for talking to the Google Sheet.
    pass