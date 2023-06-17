# Criando tuplas
dimensoes = (200, 50, 100, 1500, 3245)
# Imprimindo cada posição
print(dimensoes[0])
print(dimensoes[1])
# Criando tupla com endpoints
enpoints = ('www.uol.com.br','www.google.com.br',
            'www.g1.com.br')
# Imprimindo endpoints
print(enpoints[0])
print(enpoints)

# Percorrendo uma tupla
for i in dimensoes:
    print(f'Neste ciclo o valor de i é {i}.')
