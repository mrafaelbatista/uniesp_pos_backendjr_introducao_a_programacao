'''[FORBELLONE, 2022] Construa um algoritmo para calcular
as raízes de uma equação do 2 grau (Ax² + Bx + C), sendo
que os valores A, B, C são fornecidos pelo usuário.
(considere que a equação possui duas raizes reais).'''

import math

a = float(input("Digite o valor A: "))
b = float(input("Digite o valor B: "))
c = float(input("Digite o valor C: "))

delta = math.pow(b, 2) - 4 * a * c
if delta > 0:
    x1 = (-b + math.sqrt(delta)) / (2 * a)
    x2 = (-b - math.sqrt(delta)) / (2 * a)

    print(f"X1 -> {x1:.2f}")
    print(f"X2 -> {x2:.2f}")
    print(f"Delta -> {delta}")
else:
    print("Reduza os valores de A e C!")


