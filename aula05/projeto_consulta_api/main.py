import json
import requests
from time import sleep
from loguru import logger
from deep_translator import GoogleTranslator


URL = 'https://api.adviceslip.com/advice'
ARQUIVO = 'conselhos.txt'


def consulta_conselho(i:int) -> str:
    resposta = requests.request("GET", URL)
    mensagem = json.loads(resposta.text)
    conselho = mensagem['slip']['advice']

    logger.info(f'Conselho {i} consultado com sucesso!')

    return conselho + '\n'


def salvar_conselhos(lista_conselhos:list):

    with open(ARQUIVO, 'w', encoding='utf-8') as arquivo:
        arquivo.writelines(lista_conselhos)

    logger.info('Lista de conselhos registrada com sucesso!')


def traduzir_conselho(conselho:str) -> str:

    texto_traduzido = GoogleTranslator(
        source='english',
        target='portuguese').translate(conselho)

    logger.success('Tradução realizada com sucesso.')

    return texto_traduzido + '\n'


if __name__ == '__main__':

    # Armazenar conselhos
    conselhos = []

    for i in range(10):
        conselho = consulta_conselho((i+1))
        conselho_trad = traduzir_conselho(conselho)
        conselhos.append(conselho_trad)
        sleep(1)

    salvar_conselhos(conselhos)