import os

lista_arquivos = os.listdir('arquivos')

for i in range(len(lista_arquivos)):
    print(f'[{i}] - {lista_arquivos[i]}')

op = int(input('Escolha o arquivo desejado: '))

filename = f'arquivos\\{lista_arquivos[op]}'

with open(filename, 'r', encoding='utf-8') as arquivo:
    livro = arquivo.readlines()


for linha in livro:
    print(linha.strip())
