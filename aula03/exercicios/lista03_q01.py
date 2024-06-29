from time import sleep

contagem = 10

while contagem >= 0:
    print(f'Contagem regressiva: {contagem}')
    contagem = contagem - 1
    sleep(1)

print('Fim da contagem regressiva!')
print('FOGO!!!')