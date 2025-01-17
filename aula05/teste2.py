import json

dados = {
    "nome": "Messias",
    "idade": 38,
    "cidade": "João Pessoa"
}

with open('meu_dict.json', 'w', encoding='utf-8') as arquivo:
    json.dump(dados, arquivo, ensure_ascii=False)

with open('meu_dict.json', 'r', encoding='utf-8') as arquivo:
    dados = json.load(arquivo)

print(dados)