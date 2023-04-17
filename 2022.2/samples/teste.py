from loguru import logger
# from random import randint
#
# lista = []
#
# for i in range(20):
#     lista.append(randint(1, 10))
#
# print(lista)
# maior = -1
#
# for n in lista:
#     if n > maior:
#         print(lista.index(n))
#         maior = n

logger.info("Este é um texto")
lista = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]

resultado_diagonal_secundaria = 0

for l in range(len(lista)):
    resultado_diagonal_secundaria += lista[l][(len(lista)-1-l)]
print(resultado_diagonal_secundaria)

# Somando os valores da digonal principal
soma_diagnoal_principal = 0
for l in range(len(lista)):

    for c in range(len(lista[l])):

        if l == c:
            soma_diagnoal_principal += lista[l][c]

print(f'O valor da soma da diagonal principal é: {soma_diagnoal_principal}')