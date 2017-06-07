from flask import Flask, jsonify, abort, make_response, request
from flask_cors import CORS, cross_origin



from Modelo.Autor import Autor
from Dao.Dao import AuthorDAO, PublicacaoDAO
from Modelo.Publicacao import Publicacao

app = Flask(__name__)
CORS(app)

@app.route('/', methods=['GET'])
def get_author():
    autores = AuthorDAO()
    vetor = []
    for autor in autores.get():
        aut = Autor(autor[0], autor[1])
        vetor.append(aut.toJson())
    print(vetor)
    return jsonify({"data": vetor})


@app.route('/publicacoes', methods=['GET'])
def get_publicacao():
    publicacoes = PublicacaoDAO()
    vetor = []
    for publicacao in publicacoes.get():
        pub = Publicacao(publicacao[1])
        vetor.append(pub.toJson())
    print(vetor)
    response = jsonify({"publicacoes": vetor})
    response.headers.add('Access-Control-Allow-Origin', '*')
    return response

@app.route('/AddPub', methods=['POST'])
def set_publicacao():
    if (not request.json) or (not 'titulo') in request.json:
        print(request)
        abort(400)
    publicacoes = PublicacaoDAO()
    publicacoes.insert(request.json['titulo'])
    return ""

@app.errorhandler(404)
def not_found():
    return make_response(jsonify({'error': 'Not found'}), 404)

if __name__ == "__main__":
    app.run()