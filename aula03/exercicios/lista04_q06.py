from random import randint

caderneta = {}

qtd_alunos = int(input('Digite a quantidade de alunos: '))

for i in range(qtd_alunos):
    # nome = input('Digite o nome do aluno(a): ')
    nome = 'João ' + str(i)
    # Criando uma lista de notas vazias
    caderneta[nome] = []

    for j in range(1, 4):
        # nota = float(input(f'Digite a nota {j}: '))
        nota = randint(0, 10)
        caderneta[nome].append(nota)

print(caderneta)

for chave in caderneta:

    print(f'Aluno: {chave}')
    print(f'Nota 1: {caderneta[chave][0]}')
    print(f'Nota 2: {caderneta[chave][1]}')
    print(f'Nota 3: {caderneta[chave][2]}')

    notas = caderneta[chave]
    soma = 0

    for nota_registrada in notas:
        soma = soma + nota_registrada

    media = soma / len(notas)



