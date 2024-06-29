peso = float(input("Digite seu peso em kg: "))
altura = float(input("Digite sua altura em metros: "))

imc = peso / (altura ** 2)

if imc < 18.5:
    condicao = "abaixo do peso"
elif 18.5 <= imc < 25:
    condicao = "peso normal"
elif 25 <= imc < 30:
    condicao = "sobrepeso"
elif 30 <= imc < 35:
    condicao = "obesidade grau I"
elif 35 <= imc < 40:
    condicao = "obesidade grau II"
else:
    condicao = "obesidade grau III"

print(f"Seu IMC é {imc:.2f} - {condicao}")
