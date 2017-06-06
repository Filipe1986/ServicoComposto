import json
from flask import jsonify

class Autor():

    cpf = ""
    nome = ""

    def __init__(self, cpf, nome):
        self.cpf = cpf
        self.nome = nome

    def toJSON(self):
        return {"cpf" :self.cpf, "nome" : self.nome}