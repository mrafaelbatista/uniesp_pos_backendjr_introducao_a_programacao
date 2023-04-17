import os

# Imprima meu diretório de trabalho
print(os.getcwd())
# os.chdir('C:\\Windows\\System32')
# print(os.getcwd())
# os.makedirs("./teste1/teste2")

# path = 'C:\\Windows\\System32\\calc.exe'
# print(os.path.basename(path))
# print(os.path.dirname(path))

print(os.path.exists('C:\\Windows'))
print(os.path.exists('C:\\some_made_up_folder'))
print(os.path.isdir('C:\\Windows\\System32'))
print(os.path.isfile('C:\\Windows\\System32'))
print(os.path.isdir('C:\\Windows\\System32\\calc.exe'))
print(os.path.isfile('C:\\Windows\\System32\\calc.exe'))
