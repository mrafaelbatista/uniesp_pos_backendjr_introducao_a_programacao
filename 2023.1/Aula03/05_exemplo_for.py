from random import randint
lista_num = []

for i in range(100):
    num_aleatorio = randint(0, 1000)
    print(f'O número escolhido foi: {num_aleatorio}')
    lista_num.append(num_aleatorio)

print(lista_num)

# Contadores
n_impar = 0
n_par = 0

for j in lista_num:
    if (j % 2) == 0:
        n_par += 1
    else:
        n_impar += 1

print(f'Esta lista tem {n_par} números pares e '
      f'{n_impar} ímpares.')