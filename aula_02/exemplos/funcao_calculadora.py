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
        "Digite a opção desejada: \n"
        "1 - Somar\n"
        "2 - Subtrair\n"
        "3 - Multiplicar\n"
        "4 - Dividir\n"
        "0 - Para sair"))
    if controle != 0:
        numero1 = int(input(
            "Digite o primeiro número: "))
        numero2 = int(input(
            "Digite o segundo número: "))

        match controle:
            case 1:
                somar(numero1, numero2)
            case 2:
                subtrair(numero1, numero2)
            case 3:
                dividir(numero1, numero2)
            case 4:
                multiplicar(numero1, numero2)
    else:
        break
