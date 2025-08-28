import requests
from dotenv import load_dotenv
from data_manager import DataManager
from os import getenv
from datetime import datetime, timedelta

class FlightSearch:
    def __init__(self, city):
        self.city = city
        load_dotenv()
        self._amadeus_key = getenv("amadeus_key")
        self._amadeus_secret = getenv("amadeus_secret")
        self.get_token()
        self.today_date = datetime.now()
        self.six_month = self.today_date + timedelta(days=6*30)
        # print(self.six_month)
    
    
    def get_token(self):
        url = "https://test.api.amadeus.com/v1/security/oauth2/token"
        header = {
            "Content-Type": "application/x-www-form-urlencoded"
        }
        body = {
            'grant_type': 'client_credentials',
            'client_id': self._amadeus_key,
            'client_secret': self._amadeus_secret
        }
        
        self._token = requests.post(url,headers=header,data=body).json()["access_token"]
        
    def get_iata(self):
        url = "https://test.api.amadeus.com/v1/reference-data/locations/cities"
        header = {
            "Authorization": f"Bearer {self._token}"
        }
        for city in self.city.processed_data.index:
            body = {
                "keyword": city
            }
            iata = requests.get(url=url,headers=header,params=body).json()["data"][0]["iataCode"]
            self.city.put_iata(city,iata)
    
    def get_deal(self):
        # self.iata,self.lowest_price = self.city.get_iata()
        # if "" in self.iata:
        #     # self.get_iata()
        if True:
            url = "https://test.api.amadeus.com/v2/shopping/flight-offers"
            origin = "LON"
            header = {
            "Authorization": f"Bearer {self._token}"
            }
            body = {
                "originLocationCode": origin,
                "destinationLocationCode": "MAD",
                "departureDate": [self.today_date.strftime(f"%Y-%m-%d"), self.six_month.strftime(f"%Y-%m-%d")],
                # "returnDate": self.six_month.strftime(f"%Y-%m-%d"),
                "adults": 1,
                "maxPrice" : 1000,
                # "viewBy": "DURATION"
            }
            
            self.temp_code = (
                ("PAR", 52),
                ("FRA", 42),
                ("TYO", 485),
                ("HKG", 551),
                ("IST", 95),
                ("KUL", 414),
                ("NYC", 500),
                ("SFO", 260),
                ("DBN", 378)
            )
            for destination, price in self.temp_code: #zip(self.iata,self.lowest_price):
                # print(destination)
                # print(price)
                body["destinationLocationCode"] = destination
                body["maxPrice"] = price
                self.response = requests.get(url=url,headers=header,params=body).json()["data"]             
                if self.response != []:
                    return self.response            

class some:
    pass         
# b = DataManager()
# b = some()
# a = FlightSearch(b)
# a.get_deal()


