# with open('numeros.txt') as file_object:
#     conteudo = file_object.read()
#     print(conteudo)
#
# with open('path_file_sample\meu_nome.txt') as file_object:
#     conteudo = file_object.read()
#     print(conteudo)
#
# with open('./path_file_sample/meu_nome2.txt') as file_object:
#     conteudo = file_object.read()
#     print(conteudo)
#
# #Variável com (path + nome do arquivo)
# path = './path_file_sample/'
# file = 'welcome_to_the_jungle.txt'
# filename = path + file
#
# # Pulando linha
# with open(filename) as file_object:
#     for abacate in file_object:
#         print(abacate)
#
# #Sem pular linha
# with open(filename) as file_object:
#     for linha in file_object:
#         print(linha.rstrip())
#
# file_name = './path_file_sample/welcome_to_the_jungle.txt'
#
# with open(file_name) as file_object:
#     linhas = file_object.readlines()
#
# for linha in linhas:
#     print(linha.rstrip())
#
# file_name = './path_file_sample/writing.txt'
#
# with open(file_name, 'w') as file_object:
#     file_object.write("Eu amo programar em Java! Mentira222! \n")
#     file_object.write("Eu amo programar em Java! Mentira! \n")
#     file_object.write("Eu amo programar em Python! \n")
#
# file_name = './path_file_sample/writing.txt'
#
# with open(file_name, 'a') as file_object:
#     file_object.write("Eu amo programar em Kotlin! \n")
#     file_object.write("Chovendo... \n"
