# Bônus de Natal
valor_conta = 1000
# Depósito
deposito = float(input("Adicione um valor em sua CC: "))
valor_conta = deposito + valor_conta
# Saque
saque = float(input("Digite um valor para saque: "))

if saque > valor_conta:
    saldo = (valor_conta - saque) * - 1
    print(f"Saldo insuficiente, você precisa de: R$ {saldo:.2f}")
else:
    saldo = (valor_conta - saque)
    print(f"Restou em sua conta: R$ {saldo:.2f}")