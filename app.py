from flask import Flask, request, jsonify, render_template
from flask_cors import CORS
from database import inserir_livro, listar_livros, deletar_livro

app = Flask(__name__)
CORS(app)

@app.route('/')
def home_page():
    return render_template('index.html')

@app.route('/doar', methods=['POST'])
def doar():
    dados = request.get_json()
    titulo = dados.get('titulo')
    categoria = dados.get('categoria')
    autor = dados.get('autor')
    imagem_url = dados.get('imagem_url')

    if not all([titulo, categoria, autor, imagem_url]):
        return jsonify({'erro': 'Todos os campos são obrigatórios'}), 400
    
    inserir_livro(titulo, categoria, autor, imagem_url)
    return jsonify({"mensagem": "Livro cadastrado com sucesso"}), 201

@app.route('/livros', methods=['GET'])
def listar():
    livros = listar_livros()
    livros_formatados = [
        {"id": livro[0], "titulo": livro[1], "categoria": livro[2], "autor": livro[3], "imagem_url": livro[4]}
        for livro in livros
    ]
    return jsonify(livros_formatados)

@app.route('/livros/<int:livro_id>', methods=['DELETE'])
def deletar(livro_id):
    if deletar_livro(livro_id) == 0:
        return jsonify({"erro": "Livro não encontrado"}), 404
    return jsonify({"mensagem": "Livro deletado"})

if __name__ == '__main__':
    app.run(debug=True)
