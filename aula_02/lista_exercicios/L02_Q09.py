# Leia uma matriz 5 x 5 e escreva a localização
# (linha e a coluna) do maior valor.
from random import randint

matriz = []
for linha in range(5):
    lista_auxiliar = []
    for coluna in range(5):
        lista_auxiliar.append(randint(1, 100))
    matriz.append(lista_auxiliar)

for m in matriz:
    print(m)

maior = {'mv': 0, 'linha': None, 'coluna': None}

for linha in matriz:
    for coluna in linha:
        if coluna > maior['mv']:
            maior['mv'] = coluna
            maior['linha'] = matriz.index(linha)
            maior['coluna'] = linha.index(coluna)

print(maior)

