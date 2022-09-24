# Situação Problema 01 - Média Anual
# n1 = float(input("Digite a primeira N1: "))
# n2 = float(input("Digite a primeira N2: "))
# n3 = float(input("Digite a primeira N3: "))
# n4 = float(input("Digite a primeira N4: "))
#
# media_anual = (n1 + n2 + n3 + n4) / 4
# print(f"A média anual do aluno foi: {media_anual:.2f}")

# print("---- Sitação Problema 2 -----")
#
# raio = float(input("Digite o Raio: "))
# h = float(input("Digite a altura: "))
# PI = 3.14
#
# area_cilindro = (PI * (raio ** 2)) + (2 * PI * raio * h)
# qtd_litros = area_cilindro / 3
# qtd_latas = qtd_litros / 5
# custo_total = qtd_latas * 50.0
#
# print("Para pintar o cilindro precisamos de:")
# print(f"{qtd_latas:0.2f} latas de tinta.")
# print(f"A um custo de R$ {custo_total:0.2f}")

print("---- Sitação Problema 3 -----")

idade = int(input("Digite a sua idade: "))
ingresso = input("Ingresso VIP ou PISTA?")

if idade >= 18:
    if ingresso.upper().strip() == "VIP":
        print("Siga para o primeiro andar")
    elif ingresso.upper().strip() == "PISTA":
        print("Siga pelo corredor!")
    else:
        print("Volte para a fila e compre um ingresso!")
else:
    print("É melhor voltar pra casa!")
    print("Vou chamar o conselho tutelar!!! :(")
