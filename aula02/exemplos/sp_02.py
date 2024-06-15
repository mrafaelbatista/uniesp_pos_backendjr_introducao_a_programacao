import math

raio = float(input("Digite o raio do cilindro: "))
altura = float(input("Digite a altura do cilindro: "))

PI = 3.14

# Área do cilindro
area_lateral = 2 * PI * raio * altura
area_base = PI * (raio ** 2)
area_cilindro = area_lateral + area_base

# Cálculo da pintura
quantidade_litros = area_cilindro / 3

# A função ceil arredonda para cima
quantidade_latas = math.ceil(quantidade_litros / 5)

# Custo total
custo_total = quantidade_latas * 50

print(f"Quantidade de latas: {quantidade_latas}")
print(f"Custo total: R$ {custo_total:.2f}")

