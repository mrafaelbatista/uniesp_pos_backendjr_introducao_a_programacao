filename = 'minhas_linguagens.txt'

with open(filename, 'a', encoding='utf-8') as arquivo:
    # Lembrar do \n para pular linha
    arquivo.write('Eu amo programar em Python\n')
    arquivo.write('Eu amo programar em SQL\n')
    arquivo.write('Eu amo programar em Java\n')
