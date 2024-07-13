from random import randint

mapa_do_tesouro = []

for i in range(5):
    lista_temporaria = []

    for j in range(5):
        valor = randint(1, 200)
        print(f'Valor que vai para a matriz {valor} - Posição {[i, j]}')
        lista_temporaria.append(valor)

    mapa_do_tesouro.append(lista_temporaria)

bau_tesouro = 0
posicao = None

for linha in range(len(mapa_do_tesouro)):

    for coluna in range(len(mapa_do_tesouro[linha])):

        if mapa_do_tesouro[linha][coluna] > bau_tesouro:
            bau_tesouro = mapa_do_tesouro[linha][coluna]
            posicao = [linha, coluna]

print(f'O maior valor do mapa é: {bau_tesouro}')
print(f'A posição no mapa é {posicao}')
print(mapa_do_tesouro)


