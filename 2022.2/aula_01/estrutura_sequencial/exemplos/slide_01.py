professor = "severus snape"

print(professor.title())
print(professor.upper())
print(professor.lower())

primeiro_nome = "severus"
segundo_nome = "snape"

print((primeiro_nome + " " + segundo_nome).title())

nome_completo =\
    primeiro_nome\
    + " "\
    + segundo_nome

print("Olá, Prof." + nome_completo.title())

print("--------- Tabulação ---------")
print("Harry Potter")
print("\tHarry Potter")

print("--------- Quebra de Linha ---------")
print("HarryHermioneRonie")
print("Harry\nHermione\nRonie")

print("--------- Removendo espaços ---------")
professor = " Dumbledore "
print(professor)
# Remove espaços em branco lado esquerdo
print(professor.lstrip())
# Remove espaços em branco lado direito
print(professor.rstrip())
# Remove espaços em branco dos dois lados
print(professor.strip())

print("--------- Formatação de Strings ---------")
ano = 2022
print(f"Este ano de {ano} será maravilhoso!")
pi = 3.1438
print("O valor de pi é {:0.2f}".format(pi))
altura = 1.7718
print(f"A minha altura é de {altura:0.2f} cm.")

ano = 2022
print("Este ano de %d será maravilhoso!" % ano)
nome = "Messias"
print("Meu nome é %s" % nome)
altura = 1.7718
print("A minha altura é de %.2f cm." % altura)

print("Teste: \"Citação\"")