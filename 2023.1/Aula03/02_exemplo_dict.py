# Criando dicionários
professor = {
    'nome': 'Messias',
    'idade': 36
}

aluno = {'nome': 'Aluno 1',
         'idade': 123}

# Imprimindo valores de um dicionários
print(professor['nome'])
print(aluno['nome'])

# Criando um dicionário com vários níveis de dados
professores = {
    'Messias': {
        'idade': 36,
        'disciplinas': ['Introdução', 'Java']},
    'Wuldson': {
        'idade': 53,
        'disciplinas': ['BD I', 'BD II']}
}

# Acessando valores no meu dicionário
print(f'O professor Messias'
      f' tem {professores["Messias"]["idade"]}'
      f' anos, e ministrar as disciplinas'
      f' de {professores["Messias"]["disciplinas"]}')

# Adicionando novos dados
professores['Messias']['email'] = 'mrafaelbatista@gmail.com'
professores['Messias']['cpf'] = '000.000.000-00'
# Dicionário com novos dados
print(professores['Messias'])

# <--- Lembrando! --->
# Tipos primitivos: int, float, string, boolean
# Tipos novos: lista, tupla, dicionário

# Identificando o tipo de um dicionários
print(type(professores))

# Acessando as chaves e items
print(professores.keys())
print(professores.items())

# Tipos das chaves e items
print(type(professores.keys()))
print(type(professores.items()))

# Exemplo de delete de uma chave
print(professores)
del professores['Messias']['cpf']
print(professores)