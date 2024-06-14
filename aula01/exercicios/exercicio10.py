# Exercício do IMC (Índice de Massa Corporal)
# Escreva um programa em Python que solicite ao usuário sua altura em metros
# e seu peso em quilogramas. Calcule o Índice de Massa Corporal (IMC) usando
# a fórmula IMC = peso / (altura * altura). Exiba o resultado do IMC na tela.

# Solicita a altura do usuário
altura = float(input("Digite sua altura em metros: "))

# Solicita o peso do usuário
peso = float(input("Digite seu peso em quilogramas: "))

# Calcula o IMC
imc = peso / (altura * altura)

# Exibe o resultado
print(f"Seu IMC é: {imc:.2f}")
