import requests
from pprint import pprint
class DataManager:
    def __init__(self):
        self.endpoint = "https://api.sheety.co/f04b0bc0b4cd3207882370dfc0cd0b90/copyOfFlightDeals/prices"

    def getapi(self):
        response = requests.get(self.endpoint)
        return response.json()["prices"]

    def update_iata_code(self, row_id, new_code):
        update_url = f"{self.endpoint}/{row_id}"
        new_data = {
            "price": {
                "iataCode": new_code
            }
        }
        response = requests.put(url=update_url, json=new_data)
        print(f"Updated row {row_id}: {response.status_code}")