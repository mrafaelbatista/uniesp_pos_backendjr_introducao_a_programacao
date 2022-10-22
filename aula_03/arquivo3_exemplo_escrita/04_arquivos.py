filename = "arquivo_escrita.txt"

with open(filename, 'a') as file_object:
    file_object.write("Eu amo Python!\n")
    file_object.write("Eu amo ministrar aula!\n")