filename = 'arquivo.txt'

with open(filename, 'r', encoding='utf-8') as file_object:
    linhas_do_arquivo = file_object.readlines()

for linha in linhas_do_arquivo:
    print(f'Tipo: {type(linha)} - Texto: {linha.rstrip()}')
