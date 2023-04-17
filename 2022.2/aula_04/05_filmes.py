import csv

maior_renda = 0.0
maior_bilheteria = 0
nome_filme, nome_filme_b = '', ''
lista_selecionada = []

with open("filmes.csv", newline='', encoding='utf-8') as f:
    leitor = csv.reader(f)
    for linha in leitor:
        if linha[9] != 'Renda (R$) no ano de exibição':
            if maior_renda < float(linha[9]):
                maior_renda = float(linha[9])
                nome_filme = linha[2]

            if maior_bilheteria < int(float(linha[8])):
                maior_bilheteria = int(float(linha[8]))
                nome_filme_b = linha[2]

    # Reduzir a quantidade de dados/colunas
    # for linha in leitor:
    #     print(linha)
    #     print([linha[2], linha[8], linha[9]])
        # lista_selecionada.append(lista)

print(f"O filme é {nome_filme} com a renda de R${maior_renda}")
print(f"O filme é {nome_filme_b} com a bilheteria de {maior_bilheteria}")

print(lista_selecionada)
