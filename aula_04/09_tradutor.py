# Importações
import json
import requests
from deep_translator import GoogleTranslator


# Função que chama API do texto e API da tradução
def tradutor_eng_ptbr():
    # URL para chamada da API de texto em inglês
    url = "https://api.adviceslip.com/advice"

    # Chamada na API de texto
    resposta = requests.request("GET", url)
    mensagem = json.loads(resposta.text)
    texto = mensagem['slip']['advice']

    # Chamar API do Google Tradutor
    texto_trad = GoogleTranslator(source='english', target='portuguese').translate(texto)

    # Retornos da função o texto em inglês e o traduzido
    return texto, texto_trad


# Estrutura com 30 repetições
for i in range(30):
    # Recebe os retornos da função
    x, y = tradutor_eng_ptbr()
    # Imprime os retornos
    print(x)
    print(y)
