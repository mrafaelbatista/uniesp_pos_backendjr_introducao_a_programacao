import csv

# linha = ['Messias', 'Miguel']
linha = [
    ['Messias', 36],
    ['Mamede', 28],
    ['Carlos', 18]
         ]

with open('arquivo2_csv.csv', 'w', encoding='utf-8',
          newline='') as f:

    escritor = csv.writer(f, delimiter=';')
    # escritor.writerow(linha)
    escritor.writerows(linha)