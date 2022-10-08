# Criação da lista de altura
lista_alturas = []
# Variável de controle
controle = 5
# While para "montar" a lista com as alturas
while controle > 0:
    # Decrementa o valor de controle
    controle -= 1
    # Recebe uma altura em formato float
    altura = float(input("Digite a altura:"))
    # Adiciona a altura recebida na lista
    lista_alturas.append(altura)

print(f"Nossa lista de alturas é: {lista_alturas}")

maior_altura = 0
menor_altura = 1000

for alt in lista_alturas:

    if alt > maior_altura:
        maior_altura = alt
    elif alt < menor_altura:
        menor_altura = alt
    else:
        print(f"A altura {alt} está fora do intervalo.")

print(f"A maior altura é {maior_altura}, e a menor é {menor_altura}")