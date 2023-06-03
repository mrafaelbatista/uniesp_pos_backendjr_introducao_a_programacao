import math

PI = 3.14
altura = float(input('Digite a altura do cilindro: '))
raio = float(input('Digite o raio do cilindro: '))

area_lateral = (2 * PI * raio * altura)
area_base = PI * (raio ** 2)
area_cilindro = area_base + area_lateral
quant_total_litros = area_cilindro / 3
quant_latas = math.ceil(quant_total_litros / 5)
custo = quant_latas * 50.0

print(f'Área Lateral: {area_lateral}')
print(f'Área Base: {area_base}')
print(f'Área Cilindro: {area_cilindro}')
print(f'Quantidade Total de Litros: {quant_total_litros}')
print(f'Quantidade de Latas: {quant_latas}')
print(f'O custo total da atividade será R${custo:.2f}')