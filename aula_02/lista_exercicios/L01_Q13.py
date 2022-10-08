contador = 0
for n in range(1000, 2001, 1):
    
    if (n % 11) == 5:
        print(f"O número {n} tem resto 5.")
        contador += 1

print(f"{contador} números foram divididos por 11\
 e tiveram resto 5.")