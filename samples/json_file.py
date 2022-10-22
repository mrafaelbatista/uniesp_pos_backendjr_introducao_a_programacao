import json

x = {"001": {"nome": "Messias",
             "idade": 36,
             "signo": "Câncer",
             "ascedente": "Peixes"}
     }
# with open("meuarquivo.json", "a", encoding='utf-8') as f:
#     json.dump(x, f)

with open("meuarquivo.json", "r", encoding='utf-8') as f:
    t = json.load(f)

print(t)