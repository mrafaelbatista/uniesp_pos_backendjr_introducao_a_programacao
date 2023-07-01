print('--- Iniciando o Programa --- ')
op = input('Digite 0 sem permissão ou 1 com permissão: ')
with open('arquivo.txt', 'r', encoding='utf-8') as fo:
    for linha in fo:
        if linha[0] == op:
            print(linha[2:].rstrip())