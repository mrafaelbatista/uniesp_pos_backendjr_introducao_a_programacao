def evento(codigo):

    match codigo:
        case 1:
            return 'Porta do cofre aberta'
        case 2:
            return 'Alarme disparado'
        case 3:
            return 'Acesso não autorizado'


print(evento(3))
