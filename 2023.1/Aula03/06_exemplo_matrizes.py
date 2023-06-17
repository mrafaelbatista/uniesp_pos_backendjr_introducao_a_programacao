matriz =[[1, 2, 3], [4, 5, 6], [7, 8, 9]]

# Acessando o valor de uma matriz
print(matriz[0][1])

# Percorrendo os valores de uma matriz
for linha in matriz:
    print(linha)
    for item in linha:
        print(item)