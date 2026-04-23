import os
from flask import Flask, render_template, request
from flask_mysqldb import MySQL
import cloudinary
import cloudinary.uploader
from dotenv import load_dotenv

load_dotenv()

app = Flask(__name__)

# Configurações do MySQL usando os.getenv
app.config['MYSQL_HOST'] = os.getenv('MYSQL_HOST')
app.config['MYSQL_USER'] = os.getenv('MYSQL_USER')
app.config['MYSQL_PASSWORD'] = os.getenv('MYSQL_PASSWORD')
app.config['MYSQL_DB'] = os.getenv('MYSQL_DB')
mysql = MySQL(app)

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
    cursor.close()
    return render_template('index.html', produtos=produtos)

@app.route('/deletar', methods=['POST'])
def deletar_produto():
    id = request.form['id']
    cursor = mysql.connection.cursor()
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
    cursor = mysql.connection.cursor()
    cursor.execute("INSERT INTO produtos (titulo, descricao, img1, img2, img3) VALUES (%s, %s, %s, %s, %s)", (titulo, descricao, img1_url, img2_url, img3_url))
    mysql.connection.commit()
    cursor.close()
    return 'Produto POSTADO'

if __name__ == '__main__':
    app.run(debug=True)