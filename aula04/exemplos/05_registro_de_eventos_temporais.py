from datetime import datetime
from random import randint
from time import sleep


def evento(codigo):

    match codigo:
        case 1:
            return 'Porta do cofre aberta'
        case 2:
            return 'Alarme disparado'
        case 3:
            return 'Acesso não autorizado'
        case _:
            return 'Erro no sistema'


eventos = 0

while eventos < 10:

    sleep(randint(1, 3))
    agora = datetime.now().strftime("%d/%m/%Y %H:%M:%S")
    mensagem = evento(randint(1, 5))

    print(f'{agora} - {mensagem.upper()}')


    # Adiciona mais 1 no valor de eventos
    eventos += 1