import sqlite3

def conectar_bd():
    return sqlite3.connect("database.db")

def criar_tabela():
    with conectar_bd() as conn, open("schema.sql", "r") as f:
        conn.executescript(f.read())
        conn.commit()

def inserir_livro(titulo, categoria, autor, imagem_url):
    with conectar_bd() as conn:
        conn.execute("""
            INSERT INTO livros (titulo, categoria, autor, imagem_url)
            VALUES (?, ?, ?, ?)""",
            (titulo, categoria, autor, imagem_url))
        conn.commit()

def listar_livros():
    with conectar_bd() as conn:
        return conn.execute("SELECT * FROM livros").fetchall()

def deletar_livro(livro_id):
    with conectar_bd() as conn:
        cursor = conn.cursor()
        cursor.execute("DELETE FROM livros WHERE id = ?", (livro_id,))
        conn.commit()
    return cursor.rowcount

criar_tabela()