num_rifa = 0

while num_rifa < 1000:
    # num_rifa = num_rifa + 1
    num_rifa += 1
    print(f'Número da Rifa: {num_rifa}')

# Exemplo
controle = 0
while True:
    print(f'{controle} - O Vasco é o melhor do Brasil!!!')
    controle += 1
    if controle > 1000:
        break

# Situação Problema 2
while True:
    nome = input('Digite seu nome: ')
    if nome.upper() == 'seu nome'.upper():
        break