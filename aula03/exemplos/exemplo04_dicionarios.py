professor = {
    'nome': 'Messias',
    'idade': 26,
}

print(professor)
print(professor['nome'])
print(professor['idade'])

print('----')
professor['nome'] = 'Messi'
professor['idade'] = 35
print(professor)
print(professor['nome'])
print(professor['idade'])

professor['email'] = ['mrafaelbatista@gmail.com']

print(professor)

del professor['idade']

print(professor)