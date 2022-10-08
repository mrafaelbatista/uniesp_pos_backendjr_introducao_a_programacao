# Importação da função randomica inteira
from random import randint

# Criação da minha lista
lista_num = []

for n in range(100):
    lista_num.append(randint(1, 1000))

# Variáveis de contagem
val_pares = 0
val_impares = 0

for i in lista_num:
    # O % representa o resto da divisão 10 / 2 = 5, com resto 0
    # Se um número tem resto 0, quando divido por 2, ele é par
    if (i % 2) == 0:
       val_pares += 1
    else:
        val_impares += 1

print(f"A minha lista é:\n {lista_num}")
print(f"Quantidade de valores pares: {val_pares}")
print(f"Quantidade de valores ímpares: {val_impares}")
