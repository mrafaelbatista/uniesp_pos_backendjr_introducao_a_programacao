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
# else é utilizado quando as condicionais são falsas
else:
    print(f"{nome}, você não pode entrar na festa.")

# ---- Finalize sua programação ----

print("Finalizando o programa.")