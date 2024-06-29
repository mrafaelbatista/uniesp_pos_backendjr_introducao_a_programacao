num1 = int(input("Digite o primeiro número: "))
num2 = int(input("Digite o segundo número: "))

if num1 > num2:
    print(f"O número {num1} é maior que o número {num2}.")
elif num1 < num2:
    print(f"O número {num2} é maior que o número {num1}.")
else:
    print(f"Os números {num1} e {num2} são iguais.")
