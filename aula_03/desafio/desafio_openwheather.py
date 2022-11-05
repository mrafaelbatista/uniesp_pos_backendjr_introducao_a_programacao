import requests
import json

API_KEY = ''
LAT = -5.79448
LOG = -35.211
url = (f"https://api.openweathermap.org/data/2.5/weather?lat={LAT}&lon={LOG}&appid={API_KEY}")

resposta = requests.request("GET", url)
objetos = json.loads(resposta.text)
# dados = objetos['dados']

for i in objetos:
    print(f"{i} :: {objetos[i]}")
