texto = input("Digite um texto: ")
contagem = {}

for letra in texto:
    if letra.isalpha():
        letra = letra.lower()
        if letra in contagem:
            contagem[letra] += 1
        else:
            contagem[letra] = 1

for letra, quantidade in contagem.items():
    print(f"A letra '{letra}' aparece {quantidade} vezes.")
