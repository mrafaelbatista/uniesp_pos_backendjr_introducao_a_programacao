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

# Método remove
frutas.remove("morango")
print(frutas)

frutas = ["pêra", "uva", "maçã", "kiwi"]
print(frutas)
indice = frutas.index('uva')
pop_fruta = frutas.pop(indice)
print(frutas)
print(f"Você tirou {pop_fruta} da sua sacola de frutas!")

# Minha primeira tupla :)
t_numbers = (10, 20, 30)
print(t_numbers[0])
print(t_numbers)

# Tentando alterando o valor de um objeto da tupla
# E isso deu erro :/
# t_numbers[0] = 1000
# print(t_numbers[0])

# Alterando (sobrescrevendo) uma tupla
t_numbers = (100, 200)
print(t_numbers)

print("\n---- Dicionários -----\n")
professor = {'nome':'Messias', 'idade': 36,
             'email': 'mrafaelbatista@gmail.com'}
print(professor['nome'])
print(f"Meu nome é {professor['nome']}")

# Adicionar uma nova chave-valor
professor['salario'] = 30.00
print(professor)
# Adicionamos um novo valor a mesma chave
professor['salario'] = professor['salario'] * 1.1
print(professor)

# Removendo pares chave-valor
del professor['salario']
print(professor)