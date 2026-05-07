# 🦋 Brechó Borboleta — Gerenciador de Produtos
 
> Feito com ❤️ especialmente para minha mãe utilizar em seu grupo de brechó.
 
🌐 **Acesse o projeto ao vivo:** [lancador-produtos-brecho.onrender.com](https://lancador-produtos-brecho.onrender.com)
 
---
 
## 📌 Sobre o Projeto
 
O **Brechó Borboleta** é uma aplicação web completa desenvolvida do zero como primeiro projeto em Python/Flask. Nasceu de uma necessidade real: facilitar a gestão e divulgação de produtos de brechó diretamente em grupos do WhatsApp.
 
Com uma interface elegante inspirada em design editorial, é possível cadastrar produtos com fotos, título, descrição e preço — e compartilhá-los no grupo com um clique. O sistema conta com painel administrativo protegido por login, histórico de vendas e dashboard financeiro.
 
---
 
## ✨ Funcionalidades
 
### 👥 Público geral
- 🗂️ **Vitrine de produtos** — cards elegantes com imagem, título, ID, preço e descrição
- 🔗 **Página individual** — cada produto tem sua própria URL compartilhável
- 📲 **Encomendar via WhatsApp** — envia mensagem formatada com dados do produto e link direto
### 🔐 Painel Administrativo
- 📸 **Upload de imagens** — até 3 fotos por produto (JPEG ou PNG) via Cloudinary
- 📝 **Cadastro completo** — título, descrição e preço
- ✏️ **Edição de produtos** — altere título, descrição e preço a qualquer momento
- ✅ **Marcar como vendido** — registra a venda e remove o produto automaticamente
- 📲 **Compartilhar no WhatsApp** — envia produto formatado para o grupo do brechó
- 💰 **Dashboard financeiro** — total vendido nos últimos 30 dias e total geral
---
 
## 🛠️ Tecnologias Utilizadas
 
| Tecnologia | Função |
|---|---|
| ![Python](https://img.shields.io/badge/Python-3776AB?style=flat&logo=python&logoColor=white) | Linguagem principal |
| ![Flask](https://img.shields.io/badge/Flask-000000?style=flat&logo=flask&logoColor=white) | Framework web (backend + API REST) |
| ![MySQL](https://img.shields.io/badge/MySQL-4479A1?style=flat&logo=mysql&logoColor=white) | Banco de dados (Aiven Cloud) |
| ![TailwindCSS](https://img.shields.io/badge/Tailwind_CSS-38B2AC?style=flat&logo=tailwind-css&logoColor=white) | Estilização (v4 com config customizada) |
| ![JavaScript](https://img.shields.io/badge/JavaScript-F7DF1E?style=flat&logo=javascript&logoColor=black) | Fetch API, DOM manipulation |
| ![Cloudinary](https://img.shields.io/badge/Cloudinary-3448C5?style=flat&logo=cloudinary&logoColor=white) | Hospedagem e processamento de imagens |
| ![Render](https://img.shields.io/badge/Render-46E3B7?style=flat&logo=render&logoColor=white) | Deploy e hospedagem |
 
---
 
## 🚀 Como Rodar Localmente
 
### Pré-requisitos
 
- Python 3.x
- Node.js
- MySQL
- Conta no [Cloudinary](https://cloudinary.com)
### Instalação
 
```bash
# Clone o repositório
git clone https://github.com/HenriqueStafocher/lancador_produtos_wpp.git
cd lancador_produtos_wpp
 
# Crie e ative o ambiente virtual
python -m venv venv
venv\Scripts\activate  # Windows
 
# Instale as dependências Python
pip install -r requirements.txt
 
# Instale as dependências Node.js
npm install
```
 
### Configuração
 
Crie um arquivo `.env` na raiz do projeto:
 
```env
MYSQL_HOST=localhost
MYSQL_USER=root
MYSQL_PASSWORD=sua_senha
MYSQL_DB=brecho
MYSQL_PORT=3306
 
CLOUDINARY_CLOUD_NAME=seu_cloud_name
CLOUDINARY_API_KEY=sua_api_key
CLOUDINARY_API_SECRET=seu_api_secret
 
ADMIN_USER=seu_usuario
ADMIN_PASSWORD=sua_senha_admin
SECRET_KEY=sua_chave_secreta
```
 
### Banco de Dados
 
```sql
CREATE DATABASE brecho;
USE brecho;
 
CREATE TABLE produtos (
    id INT AUTO_INCREMENT PRIMARY KEY,
    titulo VARCHAR(255) NOT NULL,
    descricao TEXT NOT NULL,
    img1 VARCHAR(500) NOT NULL,
    img2 VARCHAR(500),
    img3 VARCHAR(500),
    disponivel BOOLEAN DEFAULT TRUE,
    preco DECIMAL(10,2) NOT NULL
);
 
CREATE TABLE vendas (
    id INT AUTO_INCREMENT PRIMARY KEY,
    titulo VARCHAR(255) NOT NULL,
    preco DECIMAL(10,2),
    data DATE NOT NULL
);
```
 
### Rodando
 
```bash
# Terminal 1 — servidor Flask
python app.py
 
# Terminal 2 — compilador Tailwind CSS
npm run watch:css
```
 
Acesse `http://127.0.0.1:5000`
 
---
 
## 📁 Estrutura do Projeto
 
```
lancador_produtos_wpp/
├── static/
│   ├── assets/
│   │   └── logo_brecho.png
│   ├── input.css
│   └── output.css
├── templates/
│   ├── index.html
│   ├── login.html
│   └── produto.html
├── .env
├── .gitignore
├── app.py
├── Procfile
├── requirements.txt
├── package.json
└── README.md
```
 
---
 
## 🔐 Acesso Administrativo
 
Clique na logo do brechó na página inicial para acessar o painel de login. Após autenticação são liberados os botões de gerenciamento e o dashboard financeiro.
 
---
 
## 📖 O que Aprendi
 
Este foi meu primeiro projeto completo em Python. Desenvolvido do zero, sem experiência prévia em desenvolvimento web:
 
- ✅ Criação de APIs REST com Flask
- ✅ Integração com banco de dados MySQL
- ✅ Upload de imagens para serviços externos (Cloudinary)
- ✅ Autenticação com sessões no Flask
- ✅ Frontend responsivo com Tailwind CSS v4
- ✅ JavaScript assíncrono com Fetch API e FormData
- ✅ Variáveis de ambiente e segurança
- ✅ Deploy em produção (Render + Aiven)
- ✅ Versionamento com Git e GitHub
---
 
## 👨‍💻 Autor
 
Desenvolvido por **Henrique Stafocher** 🚀
 
[![GitHub](https://img.shields.io/badge/GitHub-HenriqueStafocher-181717?style=flat&logo=github)](https://github.com/HenriqueStafocher)
[![LinkedIn](https://img.shields.io/badge/LinkedIn-Henrique_Stafocher-0077B5?style=flat&logo=linkedin)](https://linkedin.com/in/henriquestafocher)
 
---
 
## 📄 Licença
 
Este projeto foi desenvolvido com muito carinho para o Brechó Borboleta. 🦋
