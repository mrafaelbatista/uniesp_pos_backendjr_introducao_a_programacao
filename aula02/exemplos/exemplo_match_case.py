dia_semana = int(input("Digite o dia da semana (1-7): "))

match dia_semana:
    case 1:
        print("Domingo")
    case 2:
        print("Segunda")
    case 3:
        print("Terça")
    case 4:
        print("Quarta")
    case 5:
        print("Quinta")
    case 6:
        print("Sexta")
    case 7:
        print("Sábado")
    case _:
        print(f"Valor {dia_semana} de dia da semana inválido.")