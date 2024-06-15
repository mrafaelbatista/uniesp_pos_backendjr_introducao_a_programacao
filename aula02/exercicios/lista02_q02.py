from time import sleep

print("--- Iniciando o programa ---")
sleep(2)

temperatura = float(input("Digite a temperatura: "))
escala = input("Digite a escala (C ou F): ").upper()

resultado = 0

if escala == "C":
    resultado = (temperatura * 9/5) + 32
    escala = "F"

elif escala == "F":
    resultado = (temperatura - 32) * 5/9
    escala = "C"

else:
    print('Escala inválida.')

print(f"A temperatura é {resultado:.2f}°{escala}.")