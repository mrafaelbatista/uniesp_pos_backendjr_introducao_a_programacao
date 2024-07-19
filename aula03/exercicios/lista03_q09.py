numeros = [5, 8, 2, 10, 1]  # Exemplo de lista
soma_pares = 0

for numero in numeros:
    if numero % 2 == 0:
        soma_pares += numero

print(f"A soma dos números pares é: {soma_pares}")
