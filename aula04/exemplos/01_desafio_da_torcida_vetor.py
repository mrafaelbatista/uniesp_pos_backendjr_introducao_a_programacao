import time

clubes_populares = [
    'vasco', 'flamengo', 'barcelona', 'palmeiras',
    'real madrid', 'machester city', 'ibis',
    'csa', 'juventude', 'treze']

clube_coracao = input('Digite seu clube do coração: ').lower()

PRESENCA = False

for clube in range(len(clubes_populares)):

    if clube_coracao == clubes_populares[clube]:
        PRESENCA = True

if PRESENCA:
    print('Achei')
else:
    print('Não achei!')
