import datetime as dt
import requests

pixala_endpoint = "https://pixe.la/v1/users"
USERNAME = "user"
TOKEN = "yourpassword1234"
GRAPH_ID = "graph1"


user_params ={
    "token": TOKEN,
    "username": USERNAME,
    "agreeTermsOfService": "yes",
    "notMinor": "yes"
}

response = requests.post(url=pixala_endpoint, json=user_params)

graph_endpoint = f"{pixala_endpoint}/{USERNAME}/graphs"
headers = {
    "X-USER-TOKEN": TOKEN
}
graph_config = {
    "id": GRAPH_ID,
    "name": "Cycling Graph",
    "unit": "Km",
    "type": "float",
    "color": "ajisai"
}

graph_response = requests.post(url=graph_endpoint, json=graph_config, headers=headers)
print(graph_response.text)

pixel_endpoint = f"{graph_endpoint}/{GRAPH_ID}"

day1 = dt.datetime(year=2023, month=2, day=23).strftime("%Y%m%d")
day2 = dt.datetime(year=2023, month=2, day=24).strftime("%Y%m%d")
days = [day1, day2]
quantity1 = "7.4"
quantity2 = "12.2"
quantities = [quantity1, quantity2]

for i in range(len(days)):
    pixel_config = {
        "date": days[i],
        "quantity": quantities[i]
    }
    pixel_response = requests.post(url=pixel_endpoint, json=pixel_config, headers=headers)
    print(pixel_response.text)

pixel_update_endpoint = f"{pixel_endpoint}/{day1}"
pixel_update_config = {
    "quantity": "3.8",
}
pixel_update_response = requests.put(url=pixel_update_endpoint, json=pixel_update_config, headers=headers)
print(pixel_update_response.text)

pixel_delete_endpoint = f"{pixel_endpoint}/{day1}"
pixel_delete_response = requests.delete(url=pixel_delete_endpoint, headers=headers)


