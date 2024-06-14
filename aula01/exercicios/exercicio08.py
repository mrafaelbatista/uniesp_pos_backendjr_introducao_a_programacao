# Exercício da Conversão de Moedas
# Escreva um programa em Python que solicite ao usuário um valor em Real (BRL)
# e faça a conversão desse valor para Dólar Americano (USD). Considere a taxa
# de câmbio fixa de 1 USD = 5 BRL. Exiba o valor convertido na tela.

# Solicita o valor em Real
real = float(input("Digite o valor em Real (BRL): "))

# Calcula o valor em Dólar
dolar = real / 5

# Exibe o resultado
print(f"O valor em Dólar é: {dolar:.2f}")
