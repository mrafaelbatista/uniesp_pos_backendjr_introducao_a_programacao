from random import randint

vetor_a = []

for i in range(10):
    vetor_a.append(randint(10, 30))

x = int(input('Digite o número secreto: '))

vetor_m = []

for i in range(len(vetor_a)):
    resultado = vetor_a[i] * x
    vetor_m.append(resultado)

print(vetor_a)
print(vetor_m)
print(f'Multiplicador: {x}')