import pandas as pd

data = {'deal': [
    {'city': 'Paris', 'iataCode': '1', 'lowestPrice': 54, 'id': 2},
    {'city': 'Frankfurt', 'iataCode': '10', 'lowestPrice': 42, 'id': 3},
    {'city': 'Tokyo', 'iataCode': '', 'lowestPrice': 485, 'id': 4},
    {'city': 'Hong Kong', 'iataCode': '', 'lowestPrice': 551, 'id': 5},
    {'city': 'Istanbul', 'iataCode': '', 'lowestPrice': 95, 'id': 6},
    {'city': 'Kuala Lumpur', 'iataCode': '4', 'lowestPrice': 414, 'id': 7},
    {'city': 'New York', 'iataCode': '', 'lowestPrice': 240, 'id': 8},
    {'city': 'San Francisco', 'iataCode': '', 'lowestPrice': 260, 'id': 9},
    {'city': 'Dublin', 'iataCode': '', 'lowestPrice': 378, 'id': 10}
]}

df = pd.DataFrame.from_dict(data["deal"]).set_index("city")
# print(df["iataCode"].values)
a = df["id"].values.tolist()
c = df["iataCode"].values.tolist()

# print(c.tolist())

for x,b in zip(a,c):
    print(x)
    print("_")
    print(b)
    

# # import requests

# # url = "https://test.api.amadeus.com/v1/security/oauth2/token"
# # amadeus_key="I4f8IkHGzNKMXMEME5l0Tlkcri6n4zN4"
# # amadeus_secret="LjSwwGuKpZBEMtFt"
# # header = {
# #     "Content-Type": "application/x-www-form-urlencoded"
# # }
# # body = {
# #     'grant_type': 'client_credentials',
# #     'client_id': amadeus_key,
# #     'client_secret': amadeus_secret
# # }

# # response = requests.post(url,headers=header,data=body)
# # print(response.json())

# from datetime import datetime
# from datetime import timedelta
# today_date = datetime.now()
# print(today_date + timedelta(days=30*6))


# a = (10,11)
# c,b = a
# print(c)