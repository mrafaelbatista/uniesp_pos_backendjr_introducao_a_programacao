print('--- Iniciando programa da idade ---')

idade = int(input('Digite a sua idade: '))

if 17 < idade < 100:
    print('Você pode ir ao guichê!')
    tipo_ingresso = input('Qual seu ingresso VIP ou PISTA: ')
    tipo_ingresso = tipo_ingresso.upper()
    print(f'Meu tipo de ingresso é {tipo_ingresso}')

    if tipo_ingresso == 'VIP':
        print('Pode seguir para o PRIMEIRO ANDAR!')
    elif tipo_ingresso == 'PISTA':
        print('Vá em direção a PISTA!')
    else:
        print('Seu ingresso não é válido!')
else:
    print('Você não tem a idade permitida!')
