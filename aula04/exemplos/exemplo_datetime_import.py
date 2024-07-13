import datetime

# Obtém a data e hora atuais
agora = datetime.datetime.now()

# Formata a data e hora em uma string legível
data_formatada = agora.strftime("%d/%m/%Y %H:%M:%S")

print(f"Data e hora atuais: {data_formatada}")
