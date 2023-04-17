filename = 'arquivo01.txt'

with open(filename, 'r') as f_obj:
    conteudo = f_obj.read()

words = conteudo.split()
num_words = len(words)
print(num_words)