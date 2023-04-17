from random import randint

# Criamos funções para as quatro operações básicas
def somar(n1, n2):
    return n1 + n2


def subtrair(n1, n2):
    return n1 - n2


def multiplicar(n1, n2):
    return n1 * n2


def dividir(n1, n2):
    return n1 / n2


while True:
    controle = int(input(
        "1 - Somar\n"
        "2 - Subtrair\n"
        "3 - Multiplicar\n"
        "4 - Dividir\n"
        "0 - Para sair\n"
        "Digite a opção desejada: "))
    if controle != 0:
        numero1 = randint(1, 100)
        numero2 = randint(1, 100)
        print(f"O número 1 é {numero1}")
        print(f"O número 2 é {numero2}")

        if controle == 1:
            print(somar(numero1, numero2))
        elif controle == 2:
            print(subtrair(numero1, numero2))
        elif controle == 3:
            print(multiplicar(numero1, numero2))
        elif controle == 4:
            print(dividir(numero1, numero2))

    else:
        break
