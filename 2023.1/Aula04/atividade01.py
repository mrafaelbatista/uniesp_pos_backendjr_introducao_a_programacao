arquivo1 = 'contos_dos_irmaos_grimm.txt'
arquivo2 = 'o_principe_maquiavel.txt'

with open(arquivo1, 'r', encoding='utf-8') as fo:
    conteudo = fo.read()
    print(f'{len(conteudo)}')

with open(arquivo1, 'r', encoding='utf-8') as fo2:
    linhas = fo2.readlines()
    contadora = 0
    for l in linhas:
        contadora += 1
    print(f'A quantidade de linhas foi {contadora}')