messias.batista@iesp.edu.br
Whatsapp: 83 9 9609 8112


import requests
import json

API_KEY = '2f2f555888d23e5a36c5aad583ebfae9'
LAT = -5.79448
LOG = -35.211
url = (f"https://api.openweathermap.org/data/2.5/weather?lat={LAT}&lon={LOG}&appid={API_KEY}")

resposta   = requests.request("GET", url)
objetos    = json.loads(resposta.text)
# dados      = objetos['dados']

for i in objetos:
    print(f"{i} :: {objetos[i]}")

# https://api.openweathermap.org/data/2.5/weather?lat={-7.11532}&lon={-34.861}&appid={2f2f555888d23e5a36c5aad583ebfae9}