# Importações
import json
import requests
from loguru import logger
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


def salvar_traducao(texto, texto_traduzido):
    try:
        with open('frases_traduzidas.txt', 'a', encoding='utf-8') as f:
            t = texto_traduzido + "; " + texto + "\n"
            f.write(t)
    except Exception as error:
        logger.exception(error)

# Estrutura com 30 repetições
for i in range(100):
    # Recebe os retornos da função
    x, y = tradutor_eng_ptbr()
    # Salvar no arquivo
    salvar_traducao(x, y)

    # # Imprime os retornos
    # print(x)
    # print(y)
