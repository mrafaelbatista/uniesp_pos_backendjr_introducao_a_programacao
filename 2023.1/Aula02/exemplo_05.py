print('--- Iniciando o programa da idade ---')

ano_nascimento = int(input('Digite seu ano de nascimento: '))
idade = 2023 - ano_nascimento

if idade >= 18:
    print('Você pode dirigir e votar.')
elif 15 < idade < 18:
    print('Você não pode dirigir, mas pode votar.')
else:
    print('Você ainda é muito novo para essas atividades.')

print(f'Sua idade é: {idade}')