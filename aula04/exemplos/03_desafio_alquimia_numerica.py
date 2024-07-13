from random import randint

vetor_a = []
vetor_b = []

for i in range(10):
    vetor_a.append(randint(100, 500))
    vetor_b.append(randint(500, 999))

print('Vetor a')
print(vetor_a)
print('Vetor b')
print(vetor_b)

vetor_n = []

for i in range(len(vetor_a)):
    soma = vetor_a[i] + vetor_b[i]
    vetor_n.append(soma)

print('Vetor n')
print(vetor_n)