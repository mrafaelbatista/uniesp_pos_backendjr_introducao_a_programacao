
with open('arquivo.txt', 'r', encoding='utf-8') as file_object:
    conteudo = file_object.read()
    print(f'Tipo: {type(conteudo)} \n{conteudo}')