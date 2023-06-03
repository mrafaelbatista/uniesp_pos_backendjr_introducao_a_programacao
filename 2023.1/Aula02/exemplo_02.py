print('--- Iniciando programa da idade ---')

idade = int(input('Digite a sua idade: '))
tipo_ingresso = input('Digite o tipo ingresso VIP ou PISTA: ')
tipo_ingresso = tipo_ingresso.upper()

# Estrutura condicional IF
if idade >= 18 and tipo_ingresso == 'VIP':
    print('Você pode entrar na festa!')
    print('Pode seguir para o primeiro andar!')

elif idade >= 18 and tipo_ingresso == 'PISTA':
    print('Você pode entrar na festa!')
    print('Pode seguir para a pista!')

else:
    print('Você não pode entrar na festa')

print('--- Fim do programa ---')