import requests

url = 'https://api.adviceslip.com/advice'

for i in range(10):
    resposta = requests.get(url)
    resposta = resposta.json()
    print(resposta['slip']['advice'])