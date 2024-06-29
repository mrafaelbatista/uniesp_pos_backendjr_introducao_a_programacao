saldo = float(input("Digite o valor do depósito inicial: "))

valor_saque = float(input("Digite o valor do saque: "))
saldo -= valor_saque

if saldo >= 0:
    print(f"Saldo positivo: R${saldo:.2f}")
else:
    debito = -saldo
    print(f"Saldo negativo: R${saldo:.2f}. Débito de R${debito:.2f}")
