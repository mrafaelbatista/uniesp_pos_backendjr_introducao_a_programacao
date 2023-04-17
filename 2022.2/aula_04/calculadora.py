class Calculadora():

    def __init__(self, marca):
        self.marca = marca

    def somar(self, n1, n2):
        return n1 + n2

    def subtrair(self, n1, n2):
        return n1 - n2

    def multiplicar(self, n1, n2):
        return n1 * n2

    def dividir(self, n1, n2):
        return n1 / n2

    def potenciacao(n1, n2):
        return n1 ** n2


casio = Calculadora("casio")
soma = casio.somar(2, 6)
print(soma)