# Situação Problema 01 - Média Anual
# n1 = float(input("Digite a primeira N1: "))
# n2 = float(input("Digite a primeira N2: "))
# n3 = float(input("Digite a primeira N3: "))
# n4 = float(input("Digite a primeira N4: "))
#
# media_anual = (n1 + n2 + n3 + n4) / 4
# print(f"A média anual do aluno foi: {media_anual:.2f}")

print("---- Sitação Problema 2 -----")

raio = float(input("Digite o Raio: "))
h = float(input("Digite a altura: "))
PI = 3.14

area_cilindro = (PI * (raio ** 2)) + (2 * PI * raio * h)
qtd_litros = area_cilindro / 3
qtd_latas = qtd_litros / 5
custo_total = qtd_latas * 50.0

print("Para pintar o cilindro precisamos de:")
print(f"{qtd_latas:0.2f} latas de tinta.")
print(f"A um custo de R$ {custo_total:0.2f}")