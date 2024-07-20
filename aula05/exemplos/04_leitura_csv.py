import csv

filename = 'arquivo2.csv'

with open(filename, newline='', encoding='utf-8') as arquivo:
    reader = csv.reader(arquivo)

    # Exploração
    # for linha in reader:
    #     print(f'Tipo: {type(linha)} - Conteúdo: {linha}')

    # Nova lista com objetos limpos
    reader_limpo = []

    for linha in reader:
        # Lista iniciada vazia a cada repetição
        lista_temporaria = []

        for objeto in linha:
            # Percorrer cada coluna da minha linha
            # Limpar cada item da linha - Remover espaços em branco
            lista_temporaria.append(objeto.strip())

        reader_limpo.append(lista_temporaria)

print(reader_limpo)