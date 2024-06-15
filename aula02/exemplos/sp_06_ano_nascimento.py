from time import sleep

print("--- Iniciando o programa ---")
sleep(2)

ano_nascimento = int(input("Digite o ano do seu nascimento: "))
ANO_ATUAL = 2024

idade = ANO_ATUAL - ano_nascimento

if idade >= 18:
    print("Você pode votar e dirigir.")

elif idade >= 16:
    print("Você não pode dirigir, mas pode votar.")

print("--- Fim do programa ---")