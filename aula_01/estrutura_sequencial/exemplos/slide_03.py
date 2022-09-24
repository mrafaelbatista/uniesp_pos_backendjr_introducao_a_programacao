# Criando uma lista de nomes
nomes = ["Ademir", "Leonardo", "Carina", "Laíse"]
print(nomes)
print(type(nomes))
print(nomes[3])
print(nomes[(len(nomes)-1)])

# Criando uma lista de frutas
frutas = ["pêra", "uva", "maçã", "kiwi"]
print(frutas)

# Acessando um objeto da lista
frutas[1] = "abacate"
print(frutas)

# Inserindo um objeto na posição desejada
frutas.insert(2, "morango")
print(frutas)

frutas.insert(100, "abacaxi")
print(frutas)

# Deletando um objeto pelo index
del frutas[0]
print(frutas)

# Pesquisa o index pelo valor do objeto
print(frutas.index("kiwi"))

# Pesquisando o index, salvando na variável
# Utilizando a variável para deletar
index_fruta = frutas.index("kiwi")
del frutas[index_fruta]
print(frutas)

# Reduzindo o código, apagando com
# a função index dentro do del
del frutas[frutas.index("abacate")]
print(frutas)
