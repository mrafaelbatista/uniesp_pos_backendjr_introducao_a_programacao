class Cachorro():
    '''Modelando um cachorro'''

    def __init__(self, nome, idade):
        '''Inicializando os atributos nome e idade'''
        self.nome = nome
        self.idade = idade

    def sentar(self):
        '''Simula o cachorro sentando'''
        print(self.nome.title() + " está sentado.")

    def rolar(self):
        '''Simula o cachorro sentando'''
        print(self.nome.title() + " está rolando.")