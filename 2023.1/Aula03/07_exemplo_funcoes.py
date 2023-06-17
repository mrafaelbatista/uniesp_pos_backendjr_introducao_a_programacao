# Definindo a função calculadora
def calculadora(n1, n2):
    # Processamento da função
    resultado_soma = n1 + n2
    resultado_subt = n1 - n2
    resultado_mult = n1 * n2
    resultado_divi = n1 / n2
    # Retorno da função
    # return [resultado_soma, resultado_subt, resultado_mult, resultado_divi]
    return resultado_soma, resultado_subt, resultado_mult, resultado_divi

# print(calculadora(10, 20))
a, b, c, d = calculadora(10, 20)

print(f'Soma: {a}')
print(f'Subtracao: {b}')
print(f'Multiplicao: {c}')
print(f'Divisão: {d}')

