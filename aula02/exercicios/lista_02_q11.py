numero1 = float(input("Digite o primeiro número: "))
numero2 = float(input("Digite o segundo número: "))
operacao = input("Digite a operação (+, -, *, /): ")

match operacao:
    case "+":
        resultado = numero1 + numero2
    case "-":
        resultado = numero1 - numero2
    case "*":
        resultado = numero1 * numero2
    case "/":
        if numero2 != 0:
            resultado = numero1 / numero2
        else:
            resultado = "Divisão por zero não é permitida!"
    case _:
        resultado = "Operação inválida!"

print(f"Resultado: {resultado}")
