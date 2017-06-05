from json import JSONEncoder

class Autor():

    cpf = ""
    nome = ""

    def __init__(self, cpf, nome):
        self.cpf = cpf
        self.nome = nome