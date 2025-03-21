from flask import Flask, request, jsonify
from database import get_db, init_db

app = Flask(__name__)

@app.route('/')
def index():
    return "PREFEIÇÃO AGORA É ESSE CÓDIGO!"

@app.route('/doar', methods=['POST'])
def doar_livro():
    data = request.get_json()
    db = get_db()
    cursor = db.cursor()
    cursor.execute('''
        INSERT INTO livros (titulo, categoria, autor, imagem_url)
        VALUES (?, ?, ?, ?)
    ''', (data['titulo'], data['categoria'], data['autor'], data['imagem_url']))
    db.commit()
    return jsonify({"message": "Livro cadastrado com sucesso!"}), 201

@app.route('/livros', methods=['GET'])
def listar_livros():
    db = get_db()
    cursor = db.cursor()
    cursor.execute('SELECT * FROM livros')
    livros = cursor.fetchall()
    return jsonify([{'id': livro[0], 'titulo': livro[1], 'categoria': livro[2], 'autor': livro[3], 'imagem_url': livro[4]} for livro in livros])

if __name__ == '__main__':
    init_db(app)  
    app.run(debug=True)