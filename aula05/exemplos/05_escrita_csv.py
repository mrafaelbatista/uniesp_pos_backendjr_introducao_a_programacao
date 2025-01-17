import csv

filename = 'escrevendo.csv'

# lista = [['Messias', 38],
#          ['Luiza', 5],
#          ['João Pedro', 6],
#          ['Tio Pedro', 41]]

lista = ['Messias', 38]

with open(filename, 'w', newline='', encoding='utf-8') as arquivo:
    writer = csv.writer(arquivo, delimiter=';')

    # writer.writerows -> Armazena uma Matriz
    # writer.writerow -> Armazena uma Lista

    writer.writerow(lista)