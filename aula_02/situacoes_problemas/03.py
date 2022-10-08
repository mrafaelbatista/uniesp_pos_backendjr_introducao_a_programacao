from random import randint

print("----- Utilizando WHILE")
controle = 10
minha_lista = []

while controle >= 1:
    minha_lista.append(randint(1, 1000))
    # print(f"A minha variável controle: {controle}")
    # print(f"A minha lista: {minha_lista}")
    controle -= 1
print("Minha Lista 1")
print(minha_lista)

print("----- Utilizando FOR")

minha_lista2 = []
for n in range(100):
    minha_lista2.append(randint(1, 1000))

print("Minha lista 2")
print(minha_lista2)