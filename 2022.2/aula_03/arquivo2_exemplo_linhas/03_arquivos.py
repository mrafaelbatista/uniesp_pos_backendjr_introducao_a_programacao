filename = "arquivo03.txt"

with open(filename, "r", encoding="utf-8") as file_object:
    conteudo = file_object.readline()

print(conteudo)

for linha in conteudo:
    print(linha.rstrip())