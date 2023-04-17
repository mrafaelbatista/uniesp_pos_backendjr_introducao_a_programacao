'''Desenvolva um programa para calcular a
venda de maçãs em uma banca de feira.
O cliente compra maçãs custando R$ 1,37
cada uma, mas caso ele compre a partir de uma
dúzia pagará com desconto de 10%, portanto o
valor da unidade ficará por R$ 1,24. O programa
deverá receber o número de maçãs desejadas pelo
cliente, e retornar o valor total da compra.'''

num = int(input("Quantas maçãs você deseja? "))
total = 0
if num > 11:
    total = num * 1.24
else:
    total = num * 1.37
print(f"Sua conta deu: R$ {total:.2f}")