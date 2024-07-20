try:
    print(50/0)

except ZeroDivisionError as error:
    print(f'Erro de divisão por zero: {error}')
    print('Retornar para página principal!')

except Exception as error:
    print(error)
    print('Tentar mais 1 vez')