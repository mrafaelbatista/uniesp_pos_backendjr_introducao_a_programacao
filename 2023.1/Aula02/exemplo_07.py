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
frutas.insert(4, 'graviola')
frutas.insert(1, 'pitanga')
print(frutas)

del frutas[1]
print(frutas)
del frutas[4]
print(frutas)
frutas.insert(5, 'melancia')
print(frutas)
indice_melancia = frutas.index('melancia')
print(f'O índice da melancia é: {indice_melancia}')
del frutas[indice_melancia]
print(frutas)
frutas.remove('kiwi')
print(frutas)
print(f'O tamanho da lista é: {len(frutas)}')
frutas.insert(2, 'abacaxi')
print(frutas)
indice_abacaxi = frutas.index('abacaxi')
abacaxi_pop = frutas.pop(indice_abacaxi)
print(frutas)
print(f'A fruta deletada foi: {abacaxi_pop}')
frutas.append('Pitaya')
print(frutas)
