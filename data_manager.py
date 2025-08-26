import requests
from dotenv import load_dotenv
from os import getenv
import pandas as pd

class DataManager:
    #This class is responsible for talking to the Google Sheet.
    def __init__(self):
        load_dotenv()
        self.auth = getenv("sheety_auth")
        print(self.auth)
        self.header = {
            "Authorization": f"Bearer {self.auth}"  
        }
        
    def get(self):
        self.url = "https://api.sheety.co/23007e722a0baba09c86900023f703e6/flightDealPy/deal"
        self.get_response = requests.get(url=self.url,params=None, headers=self.header)
        self.get_data = self.get_response.json()
        self.processed_data = pd.DataFrame.from_dict(self.get_data["deal"]).set_index("city")
        
    def put(self):
        user_input = ""
        self.get()
        print(self.processed_data)
        while user_input.capitalize() != "No":
            user_input = input("Desire City? ").capitalize()
            if user_input in self.processed_data.index:
                price = int(input("How much do you want the flight to be? "))
                try:
                    self.processed_data.loc[user_input,"lowestPrice"] = price
                    self.change_id = self.processed_data.loc[user_input,"id"]
                    self.put_url = f"{self.url}/{self.change_id}"

                    self.get_data["deal"] = self.processed_data.loc[[user_input]].reset_index().to_dict(orient="records")[-1]
                    print(self.get_data)
                    self.put_response = requests.put(url=self.put_url,json=self.get_data, headers=self.header)
                except ValueError:
                    print("Enter a Value")
        # print(self.get_data)
        print(self.put_response.text)

a = DataManager()
a.put()
