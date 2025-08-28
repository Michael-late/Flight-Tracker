import requests
from dotenv import load_dotenv
from os import getenv
import pandas as pd

class DataManager:
    #This class is responsible for talking to the Google Sheet.
    def __init__(self):
        load_dotenv()
        self.auth = getenv("sheety_auth")
        self.header = {
            "Authorization": f"Bearer {self.auth}"  
        }
        self.url = "https://api.sheety.co/23007e722a0baba09c86900023f703e6/flightDealPy/deal"
        self.get_response = requests.get(url=self.url,params=None, headers=self.header)
        self.get_data = self.get_response.json()
        self.processed_data = pd.DataFrame.from_dict(self.get_data["deal"]).set_index("city")
    
    def search_id(self,city):
        self.change_id = self.processed_data.loc[city,"id"]
        self.put_url = f"{self.url}/{self.change_id}"
    
    def put_iata(self,city,iata):
        self.search_id(city)
        self.processed_data.loc[city,"iataCode"] = iata
        self.get_data["deal"] = self.processed_data.loc[[city]].reset_index().to_dict(orient="records")[-1]
        self.put_iata_response = requests.put(url=self.put_url,json=self.get_data, headers=self.header)

    def get_iata(self):
        self.iata = self.processed_data["iataCode"].values.tolist()
        self.lowest_price = self.processed_data["lowestPrice"].values.tolist()
        return (self.iata,self.lowest_price)
    
    def put_price(self):
        user_input = ""
        print(self.processed_data)
        while user_input.capitalize() != "No":
            user_input = input("Desire City? ").title()
            if user_input in self.processed_data.index:
                price = int(input("How much do you want the flight to be? "))
                try:
                    self.processed_data.loc[user_input,"lowestPrice"] = price
                    self.search_id(user_input)
                    self.get_data["deal"] = self.processed_data.loc[[user_input]].reset_index().to_dict(orient="records")[-1]
                    print(self.get_data)
                    self.put_price_response = requests.put(url=self.put_url,json=self.get_data, headers=self.header)
                except ValueError:
                    print("Enter a Value")
        # print(self.get_data)
        print(self.put_price_response.text)

# a = DataManager()
# a.get_iata()