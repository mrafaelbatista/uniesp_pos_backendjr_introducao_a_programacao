try:
    print(50 /0)
except Exception as error:
    print(f'O erro foi: {error}')
finally:
    print('Recurso opcional!')