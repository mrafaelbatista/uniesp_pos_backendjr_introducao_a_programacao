valor_produto = float(input("Digite o valor do produto: "))
desconto_digitado = float(input("Digite o desconto: "))

desconto = valor_produto * (desconto_digitado / 100)
valor_final = valor_produto - desconto

print(f"Valor Produto: {valor_produto}")
print(f"Desconto: {desconto}")
print(f"Valor Final: {valor_final}")
