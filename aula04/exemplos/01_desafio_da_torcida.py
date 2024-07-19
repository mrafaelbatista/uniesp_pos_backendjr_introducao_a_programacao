clubes_populares = [
    'vasco', 'flamengo', 'barcelona', 'palmeiras',
    'real madrid', 'machester city', 'ibis',
    'csa', 'juventude', 'treze']

clube_coracao = input('Digite seu clube do coração: ').lower()

for clube in clubes_populares:
    if clube == clube_coracao:
        print(f'Achei o {clube}')
    else:
        print(f'Não achei! - {clube}')
