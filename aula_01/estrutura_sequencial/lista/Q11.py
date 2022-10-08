lista_convidados = ['Luke Skywalker', 'Thor', 'Seu Madruga']

for i in lista_convidados:
    mensagem = f"Ei, {i}, vamos para a balada!"
    print(mensagem)

print('Seu Madruga, precisou vender churros!!!')
lista_convidados.remove('Seu Madruga')

lista_convidados.insert(0, 'Spock')
lista_convidados.insert(1, 'Viúva Negra')
lista_convidados.insert(len(lista_convidados), 'Smigol')

for i in lista_convidados:
    mensagem = f"Ei, {i}, vamos para a balada!"
    print(mensagem)