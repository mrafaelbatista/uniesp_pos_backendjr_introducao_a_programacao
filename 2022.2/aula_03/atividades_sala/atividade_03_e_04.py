import os
from loguru import logger

def contador_palavras(filename):
    try:

        with open(filename, 'r', encoding="utf-8") as file_object:
            conteudo = file_object.read()
        palavras = conteudo.split()
        return len(palavras)

    except FileNotFoundError as error:
        logger.error(error)
    except Exception as error:
        logger.error(error)


def guardar_info(titulo, quant_palavras, quant_bytes):

    info = f"" \
           f"Titulo: {titulo}; " \
           f"Qtd Palavras: {quant_palavras}; " \
           f"Qtd MB: {quant_bytes}\n"
    try:

        with open("database.txt", "a", encoding="utf-8") as file_object:
            file_object.write(info)

    except (FileNotFoundError, Exception) as error:
        logger.error(error)



def ler_database():

    try:

        with open("database.txt", "r", encoding="utf-8") as file_object:
            for linha in file_object:
                print(linha.rstrip())

    except (FileNotFoundError, Exception) as error:
        logger.error(error)

opcao = 10

while True:


    try:
        opcao = int(input(
            "1 - The Prince\n"
            "2 - A Book Of German Lyric\n"
            "3 - The eBook is 40\n"
            "9 - Ler Base de Dados\n"
            "0 - Sair "
        ))

    except Exception as error:
        logger.error(error)

    if opcao == 1:
        try:
            filename = 'the_prince_.txt'
            print(f"O livro tem:\n{contador_palavras(filename)}")
            guardar_info(
                "The Prince",
                contador_palavras(filename),
                (os.path.getsize(filename)/1000000)
            )
        except (FileNotFoundError, Exception) as error:
            logger.error(error)

    elif opcao == 2:
        try:
            filename = "a_book_of_german_lyric.txt"
            print(contador_palavras("a_book_of_german_lyric.txt"))
            guardar_info(
                "A book of German Lyric",
                contador_palavras("a_book_of_german_lyric.txt"),
                (os.path.getsize("a_book_of_german_lyric.txt")/1000000)
            )
        except (FileNotFoundError, Exception) as error:
            logger.error(error)

    elif opcao == 3:
        try:
            filename = "the_ebook_is_40.txt"
            print(contador_palavras("the_ebook_is_40.txt"))
            guardar_info(
                "The Ebook is 40",
                contador_palavras("the_ebook_is_40.txt"),
                (os.path.getsize("the_ebook_is_40.txt")/1000000)
            )
        except (FileNotFoundError, Exception) as error:
            logger.error(error)

    elif opcao == 9:

        ler_database()

    elif opcao == 0:
        break