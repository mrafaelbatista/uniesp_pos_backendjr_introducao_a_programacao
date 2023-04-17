h = float(input("Digite o valor da altura do cilindro: "))
r = float(input("Digite o valor do raio do cilindro: "))
PI = 3.14
area = (PI * (r ** 2)) + (2 * PI * r * h)
litro = area / 3
quantidade_latas = litro / 5
custo = quantidade_latas * 50
print(f"O custo é de R$ {custo:%.2f} e a quantidade litros {quantidade_latas:%.2f}")