import audioop
from flask import Flask, jsonify
from Dao import AuthorDAO
from Modelo.Autor import Autor

app = Flask(__name__)

@app.route('/', methods=['GET'])
def metodo():
    autores = AuthorDAO()
    vetor = []
    for autor in autores.get():
        aut = Autor(autor[0],autor[1])
        vetor.append(aut)
    print(vetor)
    return jsonify({"autores" : vetor})

if __name__ == "__main__":
    app.run()