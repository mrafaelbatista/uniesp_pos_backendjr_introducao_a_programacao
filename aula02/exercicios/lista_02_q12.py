numero_dia = int(input("Digite um número de 1 a 7: "))

match numero_dia:
    case 1:
        dia_semana = "Domingo"
    case 2:
        dia_semana = "Segunda-feira"
    case 3:
        dia_semana = "Terça-feira"
    case 4:
        dia_semana = "Quarta-feira"
    case 5:
        dia_semana = "Quinta-feira"
    case 6:
        dia_semana = "Sexta-feira"
    case 7:
        dia_semana = "Sábado"
    case _:
        dia_semana = "Número inválido!"

print(f"Dia da semana: {dia_semana}")
