import projeto_funcoes
from datetime import datetime

lista_nomes = projeto_funcoes.ler_arquivo()

while True:

    print('1 - Adicionar\n'
          '2 - Pesquisar\n'
          '3 - Listar\n'
          '4 - Remover\n'
          '5 - Alterar\n'
          '6 - Salvar em arquivo\n'
          '7 - Ler do arquivo\n'
          '0 - Sair')

    opcao = int(input('Digite a opção desejada: '))

    match opcao:
        case 1:
            lista_nomes = projeto_funcoes.adicionar(lista=lista_nomes)
            print(f'{datetime.now()} - Usuário adicionado com sucesso!')

        case 2:
            projeto_funcoes.pesquisar(lista=lista_nomes)
            print(f'{datetime.now()} - Pesquisa realizada com sucesso!')

        case 3:
            projeto_funcoes.listar(lista=lista_nomes)
            print(f'{datetime.now()} - Lista gerada com sucesso!')

        case 4:
            lista_nomes = projeto_funcoes.remover(lista=lista_nomes)
            print(f'{datetime.now()} - Usuário removido com sucesso!')

        case 5:
            lista_nomes = projeto_funcoes.alterar(lista=lista_nomes)
            print(f'{datetime.now()} - Usuário alterado com sucesso!')

        case 6:
            projeto_funcoes.salvar_arquivo(lista=lista_nomes)
            print(f'{datetime.now()} - Usuários persistidos com sucesso!')

        case 7:
            lista_nomes = projeto_funcoes.ler_arquivo()
            print(f'{datetime.now()} - Arquivo recuperado com sucesso!')

        case 0:
            print(f'Programa finalizando...')
            break
