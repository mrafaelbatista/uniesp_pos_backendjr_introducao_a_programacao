# Declarando uma lista
nomes = ['Messias', 'Verônica', 'Miguel', 'Gabriela']

print(nomes)
print(f'O tipo do dado é: {type(nomes)}')
print(f'Imprimindo a posição 0 -> {nomes[0]}')

print('--- Frutas')

frutas = ['pêra', 'uva', 'maçã', 'kiwi']
print(frutas)
frutas[1] = 'abacate'
print(frutas)
frutas.insert(2, 'morango')
print(frutas)