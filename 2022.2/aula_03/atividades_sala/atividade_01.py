filename = "the_prince_.txt"

with open(filename, 'r', encoding="utf-8") as file_object:
    conteudo = file_object.read()

quantidade_palavras = conteudo.split()
print(len(quantidade_palavras))
