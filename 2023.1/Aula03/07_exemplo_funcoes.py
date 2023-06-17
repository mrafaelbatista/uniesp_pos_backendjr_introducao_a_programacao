def calculadora(n1, n2):

    resultado_soma = n1 + n2
    resultado_subt = n1 - n2
    resultado_mult = n1 * n2
    resultado_divi = n1 / n2

    return resultado_soma, resultado_subt, resultado_mult, resultado_divi

# print(calculadora(10, 20))
a, b, c, d = calculadora(10, 20)

print(f'Soma: {a}')
print(f'Subtracao: {b}')
print(f'Multiplicao: {c}')
print(f'Divisão: {d}')