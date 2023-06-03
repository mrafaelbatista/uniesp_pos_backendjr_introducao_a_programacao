print('--- Iniciando o Cálculo do Peso Ideal ---')

genero = input('Digite seu gênero (M ou F): ').upper()
altura = float(input('Digite sua altura: '))

if genero == 'F':
    peso_ideal = (62.1 * altura) - 44.7
elif genero == 'M':
    peso_ideal = (72.7 * altura) - 58
else:
    print('Gênero incorreto!')

print(f'Você que é do gênero {genero}'
      f' tem peso ideal {peso_ideal}')
