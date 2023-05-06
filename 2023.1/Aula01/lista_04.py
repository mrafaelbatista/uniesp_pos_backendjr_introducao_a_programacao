valor_produto = float(input("Digite o valor do produto R"))
# Valor do desconto / 100
valor_desconto = float(input('Digite o valor do desconto '))
valor_desconto = valor_desconto / 100

desconto = valor_desconto * valor_produto

print(f'Produto: {valor_produto}\n'
      f'Valor do desconto: {valor_desconto}\n'
      f'Desconto: {desconto}%\n'
      f'Produto com desconto: {(valor_produto - desconto)}')