import projeto_funcoes

lista_nomes = ['Messias', 'Neymar', 'Messi', 'Cristiano']

while True:

    print('1 - Adicionar\n'
          '2 - Pesquisar\n'
          '3 - Listar\n'
          '4 - Remover\n'
          '5 - Alterar\n'
          '0 - Sair')

    opcao = int(input('Digite a opção desejada: '))

    match opcao:
        case 1:
            lista_nomes = projeto_funcoes.adicionar(lista=lista_nomes)

        case 2:
            projeto_funcoes.pesquisar(lista=lista_nomes)

        case 3:
            projeto_funcoes.listar(lista=lista_nomes)

        case 4:
            lista_nomes = projeto_funcoes.remover(lista=lista_nomes)

        case 5:
            lista_nomes = projeto_funcoes.alterar(lista=lista_nomes)

        case 0:
            print(f'Programa finalizando...')
            break
