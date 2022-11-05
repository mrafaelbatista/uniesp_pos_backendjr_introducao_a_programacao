import requests
import json

Tokyo = Latitude: 35.6894, Longitude: 139.692
Ny = Latitude: 40.6643, Longitude: -73.9385
Madagascar =  Latitude: -18.9141, Longitude: 47.5306

API_KEY = ''
LAT = -5.79448
LOG = -35.211
url = (f"https://api.openweathermap.org/data/2.5/weather?lat={LAT}&lon={LOG}&appid={API_KEY}")

resposta = requests.request("GET", url)
objetos = json.loads(resposta.text)
# dados = objetos['dados']

for i in objetos:
    print(f"{i} :: {objetos[i]}")
