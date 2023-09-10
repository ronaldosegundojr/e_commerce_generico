# Criando o ambiente
from flask import Flask, render_template, request, redirect, send_file
from flask_sqlalchemy import SQLAlchemy
import mysql.connector
import csv
from sqlalchemy import create_engine

# Inicializando o ambiente
app = Flask(__name__, template_folder='template')
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = True
app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql://root:''@localhost:3306/e_commerce_v2'
engine = create_engine("mysql://root:''@localhost:3306/e_commerce_v2", echo=True)
# engine.execute('CREATE DATABASE e_commerce_v2')
# Criando o banco de dados
# engine = create_engine('mysql://root:root@localhost:3306/e_commerce_v2')
# engine.execute("CREATE DATABASE e_commerce_v2")
db = SQLAlchemy(app)

# Criando a classe do Produto
class Product(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(50), nullable=False)
    price = db.Column(db.Float, nullable=False)
    description = db.Column(db.String(200))
    available = db.Column(db.Boolean, default=True)

# Criando a classe para os Usuários
class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    user = db.Column(db.String(50), nullable=False)
    password = db.Column(db.String(50), nullable=False)
    type = db.Column(db.String(50), nullable=False)

# Criando as rotas
@app.route('/')
def index():
    return render_template('index.html')

@app.route('/products')
def products():
    products = Product.query.all()
    return render_template('/template/products/products.html', products=products)

@app.route('/report')
def report():
    products = Product.query.all()
    users = User.query.all()
    return render_template('report.html')

@app.route('/login')
def login():
    return render_template('/account/auth/login.html')

@app.route('/account')
def account():
    return render_template('/account/account.html')

@app.route('/register')
def register():
    return render_template('/account/auth/register.html')

@app.route('/export_csv', methods=['POST'])
def export_csv():
    # Estabelecendo conexão com o banco de dados
    c = mysql.connector.connect(user='root', password='root', database='e_commerce_v2')
    cursor = c.cursor()
    # Executando query para buscar os produtos
    cursor.execute("SELECT * FROM products")
    row = cursor.fetchall()
    # Escrevendo os resultados no arquivo csv
    with open('products.csv', 'w', newline='') as file:
        writer = csv.writer(file)
        writer.writerow(["name", "price", "description"])
        writer.writerows(row)
    # Fechando a conexão com o banco de dados
    c.close()
    return redirect('/products')

#### teste nova rota ########
# Rota de administração
@app.route('/admin')
def admin():
    #users = User.query.all()
    #products = Product.query.all()
    return render_template('/account/auth/admin.html') # remover o ")#" quando configurar o banco de dados ,users=users, products=products)

# Rota para criar um novo usuário
@app.route('/create_user', methods=['POST'])
def create_user():
    user = User(user=request.form['user'], password=request.form['password'], type=request.form['type'])
    db.session.add(user)
    db.session.commit()
    return redirect('/admin')

# Rota para editar um usuário
@app.route('/edit_user/<int:user_id>', methods=['POST'])
def edit_user(user_id):
    user = User.query.get_or_404(user_id)
    user.user = request.form['user']
    user.password = request.form['password']
    user.type = request.form['type']
    db.session.commit()
    return redirect('/admin')

# Rota para excluir um usuário
@app.route('/delete_user/<int:user_id>', methods=['POST'])
def delete_user(user_id):
    user = User.query.get_or_404(user_id)
    db.session.delete(user)
    db.session.commit()
    return redirect('/admin')

# Rota para criar um novo produto
@app.route('/create_product', methods=['POST'])
def create_product():
    product = Product(name=request.form['name'], price=request.form['price'], description=request.form['description'])
    db.session.add(product)
    db.session.commit()
    return redirect('/admin')

# Rota para editar um produto
@app.route('/edit_product/<int:product_id>', methods=['POST'])
def edit_product(product_id):
    product = Product.query.get_or_404(product_id)
    product.name = request.form['name']
    product.price = request.form['price']
    product.description = request.form['description']
    db.session.commit()
    return redirect('/admin')

# Rota para excluir um produto
@app.route('/delete_product/<int:product_id>', methods=['POST'])
def delete_product(product_id):
    product = Product.query.get_or_404(product_id)
    db.session.delete(product)
    db.session.commit()
    return redirect('/admin')

# Executando o ambiente
if __name__ == '__main__':
    app.run(debug=True)
    db.create_all()
