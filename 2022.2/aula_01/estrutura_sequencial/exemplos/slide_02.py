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

# print("---- Sitação Problema 3 -----")
#
# idade = int(input("Digite a sua idade: "))
#
# if idade >= 18:
#     print("Pode entrar na festa!")
#
#
# print("---- Sitação Problema 4 -----")
#
# idade = int(input("Digite a sua idade: "))
#
# if idade >= 18:
#     print("Pode entrar na festa!")
# else:
#     print("Você não pode entrar, é muito novo!")
#
# print("---- Sitação Problema 4 (ajustada) -----")
#
# idade = int(input("Digite a sua idade: "))
#
# if idade >= 18:
#     ingresso = input("Ingresso VIP ou PISTA?")
#     if ingresso.upper().strip() == "VIP":
#         print("Siga para o primeiro andar")
#     elif ingresso.upper().strip() == "PISTA":
#         print("Siga pelo corredor!")
#     else:
#         print("Volte para a fila e compre um ingresso!")
# else:
#     print("É melhor voltar pra casa!")
#     print("Vou chamar o conselho tutelar!!! :(")

# print("---- Sitação Problema 5 -----")
#
# sexo = input("Digite M ou H: ")
# altura = float(input("Digite sua altura: "))
#
# if sexo.upper().strip() == "M":
#     print((62.1 * altura) - 44.7)
# else:
#     print((72.7 * altura) - 58)

print("---- Sitação Problema 6 -----")
# from datetime import datetime
# print(datetime.now().strftime("%Y"))

ano_nascimento = int(input("Digite o ano de nascimento: "))
idade = 2022 - ano_nascimento

if idade >= 16:
    print("Parabéns, você é um eleitor!")

if idade >= 18:
    print("Você pode tentar uma auto escola!")

print("Segunda forma ---")
if idade >= 16:
    print("Parabéns, você é um eleitor!")
    if idade >= 18:
        print("Você pode tentar uma auto escola!")
else:
    print("Você precisa crescer um pouquinho mais!")
    print(f"Você tem apenas {idade} anos de vida!")