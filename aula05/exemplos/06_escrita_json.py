import json

filename = 'meu_arquivo.json'

dados = {
    'nome': 'Messias',
    'idade': 38,
    'Cidade': 'João Pessoa'
}

with open(filename, 'w', encoding='utf-8') as arquivo:
    json.dump(dados, arquivo, ensure_ascii=False)

with open(filename, 'r', encoding='utf-8') as arquivo:
    dict_json = json.load(arquivo)

print(dict_json)