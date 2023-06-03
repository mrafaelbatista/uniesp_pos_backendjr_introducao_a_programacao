''' Escreva um programa em Python que peça ao
usuário para digitar a temperatura em graus
Celsius e converta-a para Fahrenheit. A fórmula
de conversão é: Fahrenheit = (Celsius * 9/5) + 32.'''

# Solicitar temperatura em Celcius
temperatura_celcius = float(input('Digite a temperatura em graus celcius: '))

# Converter para Fahrenheit
temperatura_fahrenheit = (temperatura_celcius * 9 / 5) + 32

# Exibindo o resultado
print(f'A temperatura em Fahrenheit é {temperatura_fahrenheit}')
