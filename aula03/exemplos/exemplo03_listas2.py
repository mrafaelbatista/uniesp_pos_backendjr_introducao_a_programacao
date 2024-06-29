# Lista de frutas
frutas = ['pêra', 'uva', 'maçã', 'kiwi']
print('Lista de frutas:')
print(frutas)

# Alterando o elemento que está na posição 1
frutas[1] = 'abacate'

# Imprimir a lista
print('Lista de frutas (alterada):')
print(frutas)

frutas.insert(2, 'morango')
print('Lista de frutas (inserido morango):')
print(frutas)

# append -> Adicionando um elemento ao final da lista
frutas.append('Pitaya')
print('Lista de frutas (inserido Pitaya):')
print(frutas)

# del -> Removendo um elemento da lista
del frutas[0]
print('Lista de frutas (removido pêra):')
print(frutas)

print('\n---------------------')
frutas.append('Melancia')

if 'Melancia' in frutas:
    print(f'Índice de Melancia: {frutas.index("Melancia")}')


print('Removendo a Pitaya e a Melancia:')
frutas.remove('Pitaya')
frutas.remove('Melancia')

print('Lista de frutas (removido Pitaya e Melancia):')
print(frutas)

# pop -> Removendo o elemento da lista
fruta_removida = frutas.pop(2)
print('Lista de frutas:')
print(frutas)
print(f'Fruta removida: {fruta_removida}')







