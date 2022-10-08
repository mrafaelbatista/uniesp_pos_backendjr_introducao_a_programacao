
database = {}
# While interativo
while True:
    opcao = int(input(
        "1 - Cadastrar uma pessoa\n"
        "2 - Listar os cadastros\n"
        "3 - Deletar um cadastro\n"
        "4 - Alterar um cadastro\n"
        "0 - Sair do programa \n"
        "Digite sua opção: "
    ))

    if opcao == 1:
        codigo = int(input("Digite o código: "))
        nome = input("Digite o nome: ")
        email = input("Digite o email: ")
        data = input("Digite o dia/mês do nascimento: ")

        database[codigo] = {"nome": nome,
                            "email": email,
                            "data": data}
    elif opcao == 2:
        print(" --- LISTAGEM DE CADASTROS --- ")

        if len(database) == 0:
            print("Não existem cadastros")
        else:
            for i in database.keys():
                s = f"Nome: {database[i]['nome']} | " \
                    f"Email: {database[i]['email']} | " \
                    f"Data: {database[i]['data']}"
                print(s)
