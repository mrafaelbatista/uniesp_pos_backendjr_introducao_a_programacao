import csv

with open('arquivo_csv.csv',
          'r',
          encoding='utf-8',
          newline='') as f:

    leitor = csv.reader(f, delimiter=';')

    for l in leitor:
        print(l)