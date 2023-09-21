from flask import render_template, request, redirect
from app import  db, app
from app import Product, User
from app import app

# Criando as rotas
@app.route('/')
def index():
    return render_template('index.html')

@app.route('/products')
def products():
    products = Product.query.all()
    return render_template('products/products.html', products=products)

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