import json
from flask import jsonify


class Publicacao():
    titulo = ""


    def __init__(self, titulo):
        self.titulo = titulo

    def toJson(self):
        return {"titulo": self.titulo}