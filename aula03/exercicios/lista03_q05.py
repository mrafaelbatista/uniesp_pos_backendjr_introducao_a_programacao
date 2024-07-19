frase = input("Digite uma frase: ").lower()
contador_vogais = 0

for letra in frase:
    if letra in "aeiou":
        contador_vogais += 1

print(f"A frase possui {contador_vogais} vogais.")
