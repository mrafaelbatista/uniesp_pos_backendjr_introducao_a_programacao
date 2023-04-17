import os

print(os.getcwd())
print(os.listdir(path='.'))
print(os.path.getsize('teste_csv.py'))
totalSize = 0
for filename in os.listdir('C:\\Windows\\System32'):
    totalSize = totalSize + os.path.getsize(os.path.join('C:\\Windows\\System32', filename))
print(totalSize)
# os.chdir('C:\\Windows\\System32')
# print(os.getcwd())
# os.chdir('./')
# print(os.getcwd())
# os.chdir('C:\\Windows\\System32sadasdas')