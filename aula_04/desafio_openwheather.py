import requests
import json


def chamar_api(lat, log, nome_arquivo):
    API_KEY = '2f2f555888d23e5a36c5aad583ebfae9'
    url = (f"https://api.openweathermap.org/data/2.5/weather?lat={lat}&lon={log}&appid={API_KEY}")

    resposta = requests.request("GET", url)
    objetos = json.loads(resposta.text)

    arquivo = nome_arquivo + ".json"

    with open(arquivo, 'w', encoding='utf-8') as f:
        json.dump(objetos, f)


dl = {
    'Tokyo': {'lat': 35.6894, 'lon': 139.692},
    'NY': {'lat': 40.6643, 'lon': -73.9385},
    'Madagascar': {'lat': -18.9141, 'lon': 47.5306},
}

for index in dl.keys():
    chamar_api(
        lat=dl[index]['lat'],
        log=dl[index]['lon'],
        nome_arquivo=index)


# for i in objetos:
#     print(f"{i} :: {objetos[i]}")
