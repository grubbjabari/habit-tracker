import requests

pixela_endpoint = "https://pixe.la/v1/users"

user_params = {
    "token": "",
    "username": "",
    "agreeTermsOfService": "yes",
    "notMinor": "yes",
}

response = requests.post(url=pixela_endpoint, json=user_params)
print(response.text)


graph_endpoint = f"{pixela_endpoint}/{USERNAME}/graphs"

graph_config = {
    "id": "graph1",
    "name": "Exercise",
    "unit": "minutes",
    "type": "int",
    "color": "ajisai"
}

headers = {
   "X-USER-TOKEN": TOKEN 
}
requests.post(url=graph_endpoint, json=graph_config, headers=headers)
print(response.text)