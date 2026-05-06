import os
from flask import Flask, render_template, request, session, redirect, url_for
from flask_mysqldb import MySQL
import cloudinary
import cloudinary.uploader
from dotenv import load_dotenv

load_dotenv()

app = Flask(__name__)

app.config['MYSQL_HOST'] = os.getenv('MYSQL_HOST')
app.config['MYSQL_USER'] = os.getenv('MYSQL_USER')
app.config['MYSQL_PASSWORD'] = os.getenv('MYSQL_PASSWORD')
app.config['MYSQL_DB'] = os.getenv('MYSQL_DB')
app.config['MYSQL_PORT'] = int(os.getenv('MYSQL_PORT', 12688)) # A porta do Aiven é importante

# Configuração SSL OBRIGATÓRIA para o Aiven
app.config['MYSQL_CUSTOM_OPTIONS'] = {
    'ssl': {
        'ca': os.path.join(os.path.dirname(__file__), 'ca.pem')
    }
}
mysql = MySQL(app)

# Login Admnistrador
app.secret_key = os.getenv('SECRET_KEY')

# Configurações do Cloudinary usando os.getenv
cloudinary.config(
    cloud_name = os.getenv('CLOUDINARY_CLOUD_NAME'),
    api_key = os.getenv('CLOUDINARY_API_KEY'),
    api_secret = os.getenv('CLOUDINARY_API_SECRET')
)

@app.route('/')
def index():
    cursor = mysql.connection.cursor()
    cursor.execute('SELECT * FROM produtos WHERE disponivel = True')
    produtos = cursor.fetchall()

    cursor.execute('SELECT SUM(preco) FROM vendas')
    total_geral = cursor.fetchone()[0] or 0

    cursor.execute('SELECT SUM(preco) FROM vendas WHERE date >= DATE_SUB(NOW(), INTERVAL 30 DAY)')
    total_mensal = cursor.fetchone()[0] or 0

    cursor.close()
    return render_template('index.html', produtos=produtos, total_geral=total_geral, total_mensal=total_mensal)

@app.route('/deletar', methods=['POST'])
def deletar_produto():
    id = request.form['id']
    cursor = mysql.connection.cursor()
    cursor.execute("SELECT titulo, preco FROM produtos WHERE id = %s", (id,))
    produto = cursor.fetchone()
    cursor.execute("INSERT INTO vendas (titulo, preco, date) VALUES (%s, %s, NOW())", (produto[0], produto[1]))
    cursor.execute("DELETE FROM produtos WHERE id = %s", (id,))
    mysql.connection.commit()
    cursor.close()
    return 'Produto VENDIDO'

@app.route('/adicionar', methods=['POST'])
def adicionar_produto():
    imagens = request.files.getlist('imagens')
    img1_url = img2_url = img3_url = None
    for i, imagem in enumerate(imagens):
        resultado = cloudinary.uploader.upload(imagem)
        if i == 0:
            img1_url = resultado['secure_url']
        elif i == 1:
            img2_url = resultado['secure_url']
        elif i == 2:
            img3_url = resultado['secure_url']

    titulo = request.form['titulo']
    descricao = request.form['descricao']
    preco = request.form['preco']
    cursor = mysql.connection.cursor()
    cursor.execute("INSERT INTO produtos (titulo, descricao, preco, img1, img2, img3) VALUES (%s, %s, %s, %s, %s, %s)", (titulo, descricao, preco, img1_url, img2_url, img3_url))
    mysql.connection.commit()
    cursor.close()
    return 'Produto POSTADO'

@app.route('/login', methods=['GET'])
def login():
    return render_template('login.html')

@app.route('/login', methods=['POST'])
def fazer_login():
    usuario = request.form['usuario']
    senha = request.form['senha']
    if usuario == os.getenv('ADMIN_USER') and senha == os.getenv('ADMIN_PASSWORD'):
        session['logado'] = True
        return redirect(url_for('index'))
    else:
        return render_template('login.html', erro='Usuário ou senha incorretos')


@app.route('/produto/<int:id>')
def produto_detalhe(id):
    cursor = mysql.connection.cursor()
    cursor.execute('SELECT * FROM produtos WHERE id = %s', (id,))
    produto = cursor.fetchone()
    cursor.close()
    return render_template('produto.html', produto=produto)

@app.route('/alterar', methods=['POST'])
def alterar_produto():
    id = request.form['id']
    titulo = request.form['titulo']
    descricao = request.form['descricao']
    preco = request.form['preco']
    cursor = mysql.connection.cursor()
    cursor.execute("UPDATE produtos SET titulo = %s, descricao = %s, preco = %s WHERE id = %s", (titulo, descricao, preco, id))
    mysql.connection.commit()
    cursor.close()
    return 'ok'

if __name__ == '__main__':
    app.run(debug=True)