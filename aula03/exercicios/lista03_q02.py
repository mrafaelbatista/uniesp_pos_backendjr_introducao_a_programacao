from random import randint

numero_aleatorio = randint(1, 100)
tentativa = True

while tentativa:

    chute = int(input('Digite um número entre 1 e 100: '))

    if chute < 1 or chute > 100:
        print('O valor não é válido!')
    elif chute == numero_aleatorio:
        print('Você acertou!')
        tentativa = False
    elif chute < numero_aleatorio:
        print('O número tentado é MENOR do que o número SEGREDO!')
    else:
        print('O número tentado é MAIOR do que o número SEGREDO!')

