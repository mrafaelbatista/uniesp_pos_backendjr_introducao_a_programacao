quant_macas = int(input("Digite a quantidade de maçãs: "))
valor_total = 0

if 0 < quant_macas < 12:
    valor_total = quant_macas * 1.37
else:
    valor_total = quant_macas * 1.24

print(f'O valor total é de R$ {valor_total:.2f}')