from random import randint

lista_num = []
controle = 0

while controle < 100:
    numero_aleatorio = randint(0, 1000)
    print(f'O número escolhido foi: {numero_aleatorio}')
    lista_num.append(numero_aleatorio)
    controle += 1

print(lista_num)
