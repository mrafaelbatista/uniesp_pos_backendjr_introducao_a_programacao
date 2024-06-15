from time import sleep

print("Iniciando o programa.")

'''A função sleep serve para o programar aguardar
a quantidade de segundos definida. Neste caso, 2 segundos.'''
sleep(2)

# ---- Programe aqui ----

nome = input("Digite o seu nome: ")
idade = int(input("Digite a sua idade: "))

if idade >= 18:
    print(f"{nome}, você pode entrar na festa.")
    ingresso = input("Por favor, ingresso VIP ou PISTA? ").upper()

    if ingresso == "VIP":
        print("Siga em direção ao elevador!")

    elif ingresso == "PISTA":
        print("Siga em direção à pista!")

    else:
        print(f"{nome}, ingresso inválido.")

else:
    print(f"{nome}, você não pode entrar na festa.")

# ---- Finalize sua programação ----

print("Finalizando o programa.")