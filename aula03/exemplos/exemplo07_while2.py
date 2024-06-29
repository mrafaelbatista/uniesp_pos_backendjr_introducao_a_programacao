i = True
a = 0

while i:
    print(f'Tentativa de acesso ao Banco de Dados  n:{a}')

    if (a ** 2) > 10 ** 40:
        i = False
        print(f'Tentativa {a ** 2} de acesso ao BD com sucesso!')

    a = a + 1

print('Fim do programa!')