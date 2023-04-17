# Caminho e nome do arquivo guardado na variável
filename = "arquivo1.txt"

# Abrindo um arquivo como leitura
with open(filename, "r", encoding="utf-8") as file_object:

    # Criando uma "repetição" para ler por linhas
    for linha in file_object:

        # Imprimindo a linha lida
        print(linha.rstrip())