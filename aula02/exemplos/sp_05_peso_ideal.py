from time import sleep

print("--- Iniciando o programa ---")
sleep(2)

genero = input("Digite o seu gênero (M/F): ").upper()

if genero == "M" or genero == "F":

    altura = float(input("Digite a sua altura (ex.: 1.55): "))
    peso_ideal = -1

    if genero == "M":
        peso_ideal = (72.7 * altura) - 58

    elif genero == "F":
        peso_ideal = (62.1 * altura) - 44.7

    print(f"Para uma altura de {altura}.")
    print(f"E um gênero {genero}.")
    print(f"O seu peso ideal é {peso_ideal:.2f} kg.")

else:
    print("Gênero inválido.")


print("--- Fim do programa ---")