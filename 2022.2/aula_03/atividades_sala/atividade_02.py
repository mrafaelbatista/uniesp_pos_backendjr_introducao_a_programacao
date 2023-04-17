def contador_palavras(filename):

    with open(filename, 'r', encoding="utf-8") as file_object:
        conteudo = file_object.read()

    palavras = conteudo.split()

    return len(palavras)


while True:

    opcao = int(input(
        "1 - The Prince\n"
        "2 - A Book Of German Lyric\n"
        "3 - The eBook is 40\n"
        "0 - Sair "
    ))

    if opcao == 1:
        print(f"O livro tem:\n{contador_palavras('the_prince_.txt')}")

    elif opcao == 2:
        print(contador_palavras("a_book_of_german_lyric.txt"))

    elif opcao == 3:
        print(contador_palavras("the_ebook_is_40.txt"))

    elif opcao == 0:
        break