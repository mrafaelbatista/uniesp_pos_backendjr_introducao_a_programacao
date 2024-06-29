estoque_maximo = int(input("Digite a quantidade máxima do estoque: "))
estoque_minimo = int(input("Digite a quantidade mínima do estoque: "))
estoque_real = int(input("Digite a quantidade real do estoque: "))

media_estoque = (estoque_maximo + estoque_minimo) / 2

if estoque_real < media_estoque:
    print("É necessário adquirir mais produtos.")
elif estoque_real > media_estoque:
    print("Não é necessário adquirir mais produtos.")
else:
    print("Em breve será necessária nova aquisição de produtos.")
