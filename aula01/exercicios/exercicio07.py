# Exercício do Tempo de Viagem
# Escreva um programa em Python que solicite ao usuário a distância de uma
# viagem (em km) e a velocidade média (em km/h). Calcule o tempo de viagem
# em horas e exiba o resultado.

# Solicita a distância da viagem
distancia = float(input("Digite a distância da viagem (em km): "))

# Solicita a velocidade média
velocidade = float(input("Digite a velocidade média (em km/h): "))

# Calcula o tempo de viagem
tempo = distancia / velocidade

# Exibe o resultado
print(f"O tempo de viagem é: {tempo:.2f} horas")
