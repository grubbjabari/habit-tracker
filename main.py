import requests
import datetime

TOKEN = "qw21341dsf"
USERNAME = "user123qwerty"
GRAPH_ID = "graph1"

pixela_endpoint = "https://pixe.la/v1/users"

user_params = {
    "token": TOKEN,
    "username": USERNAME,
    "agreeTermsOfService": "yes",
    "notMinor": "yes",
}

# Use to verify and create token and username on pixela
# response = requests.post(url=pixela_endpoint, json=user_params)
# print(response.text)


graph_endpoint = f"{pixela_endpoint}/{USERNAME}/graphs"

graph_config = {
    "id": GRAPH_ID,
    "name": "Exercise",
    "unit": "minutes",
    "type": "int",
    "color": "ajisai"
}

headers = {
   "X-USER-TOKEN": TOKEN 
}

# This is to create the graph
# requests.post(url=graph_endpoint, json=graph_config, headers=headers)
# print(response.text)

today = datetime.now()

tracker_update = {
    "date": today.strftime("Y%Y%m%d"),
    "quantity": "55"
}

pixel_endpoint = graph_endpoint + "/" + GRAPH_ID

#This updates a specific point on the graph
# response = requests.post(url=pixel_endpoint, json=tracker_update, headers=headers)
# print(response.text)

update_endpoint = pixel_endpoint + "/" + today.strftime("Y%Y%m%d")

new_pixel_data = {
    "minutes" : "60"
}

#Changing a pixel
response = requests.put(url=update_endpoint, json=new_pixel_data, headers=headers)
print(response)

#Deleting a pixel
delete_endpoint = pixel_endpoint + "/" + today.strftime("Y%Y%m%d")

new_pixel_data = {
    "minutes" : "60"
}

#Changing a pixel
response = requests.put(url=delete_endpoint, json=new_pixel_data, headers=headers)
print(response)