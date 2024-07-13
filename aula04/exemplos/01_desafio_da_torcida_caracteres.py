clubes_populares = [
    'vasco', 'flamengo', 'barcelona', 'palmeiras',
    'real madrid', 'machester city', 'ibis',
    'csa', 'juventude', 'treze']

for indice in range(len(clubes_populares)):

    for letra in clubes_populares[indice]:
        print(letra)

    print(f'{clubes_populares[indice]}, tamanho: {len(clubes_populares[indice])}')