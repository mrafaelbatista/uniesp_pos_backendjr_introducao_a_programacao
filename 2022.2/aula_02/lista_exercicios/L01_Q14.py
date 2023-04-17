# Imprimir todas as tabuadas de 1 a 10
for i in range(1, 11):
    for j in range(1, 11):
        print(f"{i} x {j} = {(i*j)}")

# Pedindo uma tabuada específica
num = int(input("Digite um número:"))
for h in range(1, 11):
    print(f"{num} x {h} = {(num * h)}")