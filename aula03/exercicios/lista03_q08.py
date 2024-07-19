from random import randint

qtd_random_values = 100

# Montando lista de valores
lista_valores = []

for n in range(qtd_random_values):
    lista_valores.append(randint(1, 100000))

print(sorted(lista_valores))

maior = 0
menor = 100001

for valor in lista_valores:

    if valor > maior:
        maior = valor

    if valor < menor:
        menor = valor

print(f'O maior valor é: {maior}')
print(f'O menor valor é: {menor}')