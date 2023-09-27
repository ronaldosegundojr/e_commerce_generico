# Criando o ambiente
from flask import Flask, render_template, request, redirect, session, url_for, flash
from flask_sqlalchemy import SQLAlchemy
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
    product_id = db.Column(db.String(10), nullable=False)
    product_name = db.Column(db.String(255), nullable=False)
    description = db.Column(db.Text)
    product_img = db.Column(db.String(255))
    price = db.Column(db.DECIMAL(10, 2), nullable=False)
    discount = db.Column(db.DECIMAL(5, 2), default=0)
    final_price = db.Column(db.DECIMAL(10, 2), server_default='0.00', onupdate='price - (price * discount / 100)')
    product_date = db.Column(db.DATE)
    quantity = db.Column(db.Integer, nullable=False)


# Criando a classe para os Usuários
class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    user_privileges = db.Column(db.Integer, nullable=False)
    name = db.Column(db.String(255), nullable=False)
    username = db.Column(db.String(50), nullable=False)
    email = db.Column(db.String(255), nullable=False)
    password = db.Column(db.String(255), nullable=False)
    cellphone = db.Column(db.String(20), nullable=False)

# Criando as rotas
# Pagina inicial
@app.route('/')
def index():
    # Busque todos os produtos no banco de dados
    products = Product.query.all()
    return render_template('index.html', products=products, logged_in=session.get('logged_in'))

@app.route('/report')
def report():
    products = Product.query.all()
    users = User.query.all()
    return render_template('report.html')

######### Rotas de Usuário #########
app.secret_key = 'A0293JF0A20FKAS'
# Rota de conta
@app.route('/account')
def account():
    if is_logged_in():
        user_id = session['user_id']
        user = User.query.get(user_id)
        if user.user_privileges == 1:
            return render_template('/account/auth/admin.html', user=user)
        else:
            return render_template('/account/auth/user.html', user=user)
    else:
        return redirect(url_for('login'))

# Rota de logout
@app.route('/logout')
def logout():
    session.clear()  # Limpa a sessão, efetivamente fazendo logout
    return redirect(url_for('login'))

# Rota de login
@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']
        
        # Consulta o banco de dados para verificar se o usuário existe
        user = User.query.filter_by(username=username, password=password).first()
        
        if user:
            session['logged_in'] = True
            session['user_id'] = user.id  # Armazena o ID do usuário na sessão
            flash('Login bem-sucedido!', 'success')  # Exibe uma mensagem de sucesso

            if user.user_privileges == 1:
                # O usuário é um administrador, redirecionar para /admin
                return redirect(url_for('admin'))
            else:
                # O usuário não é um administrador, redirecionar para /account
                return redirect(url_for('account'))
        else:
            flash('Credenciais incorretas. Tente novamente.', 'danger')  # Exibe uma mensagem de erro
            return redirect(url_for('login'))
    
    return render_template('account/auth/login.html')

#### Rotas de ADMIN ########
# Função para verificar se o usuário está logado
def is_logged_in():
    return 'user_id' in session

# Rota de administração
@app.route('/admin')
def admin():
    if is_logged_in():
        user_id = session['user_id']
        user = User.query.get(user_id)
        if user.user_privileges == 1:
            # O usuário é um administrador, renderizar a página de admin
            users = User.query.all()
            products = Product.query.all()
            return render_template('/account/auth/admin.html', users=users, products=products)
    # Se não for um administrador ou não estiver logado, redirecionar para /login
    return redirect(url_for('login'))



# Rota para criar um novo usuário
@app.route('/create_user', methods=['POST'])
def create_user():
    user_privileges = request.form['user_privileges']
    name = request.form['name']
    username = request.form['username']
    email = request.form['email']
    password = request.form['password']
    cellphone = request.form['cellphone']
    
    user = User(user_privileges=user_privileges, name=name, username=username, email=email, password=password, cellphone=cellphone)
    db.session.add(user)
    db.session.commit()
    return redirect('/admin')

# Rota para editar um usuário
@app.route('/edit_user/<int:user_id>', methods=['POST'])
def edit_user(user_id):
    user = User.query.get_or_404(user_id)
    
    user_privileges = request.form['user_privileges']
    name = request.form['name']
    username = request.form['username']
    email = request.form['email']
    password = request.form['password']
    cellphone = request.form['cellphone']
    
    user.user_privileges = user_privileges
    user.name = name
    user.username = username
    user.email = email
    user.password = password
    user.cellphone = cellphone
    
    db.session.commit()
    return redirect('/admin')

# Rota para excluir um usuário
@app.route('/delete_user/<int:user_id>', methods=['POST'])
def delete_user(user_id):
    user = User.query.get_or_404(user_id)
    db.session.delete(user)
    db.session.commit()
    return redirect('/admin')

# Rota para visualizar todos os usuários
@app.route('/view_users')
def view_users():
    users = User.query.all()
    return render_template('/account/auth/view_users.html', users=users)


######### Rotas de Produtos #########

# Rota para listar todos os produtos
@app.route('/products')
def products():
    products = Product.query.all()
    return render_template('products/products.html', products=products)

# Rota para criar um novo produto
@app.route('/create_product', methods=['POST'])
def create_product():
    product_id = request.form['product_id']
    product_name = request.form['product_name']
    description = request.form['description']
    product_img = request.form['product_img']
    price = request.form['price']
    discount = request.form['discount']
    product_date = request.form['product_date']
    quantity = request.form['quantity']
    
    product = Product(product_id=product_id, product_name=product_name, description=description, product_img=product_img, price=price, discount=discount, product_date=product_date, quantity=quantity)
    db.session.add(product)
    db.session.commit()
    return redirect('/admin')

# Rota para editar um produto
@app.route('/edit_product/<int:product_id>', methods=['POST'])
def edit_product(product_id):
    product = Product.query.get_or_404(product_id)
    
    product_id = request.form['product_id']
    product_name = request.form['product_name']
    description = request.form['description']
    product_img = request.form['product_img']
    price = request.form['price']
    discount = request.form['discount']
    product_date = request.form['product_date']
    quantity = request.form['quantity']
    
    product.product_id = product_id
    product.product_name = product_name
    product.description = description
    product.product_img = product_img
    product.price = price
    product.discount = discount
    product.product_date = product_date
    product.quantity = quantity
    
    db.session.commit()
    return redirect('/admin')

# Rota para excluir um produto
@app.route('/delete_product/<int:product_id>', methods=['POST'])
def delete_product(product_id):
    product = Product.query.get_or_404(product_id)
    db.session.delete(product)
    db.session.commit()
    return redirect('/admin')

# Rota para visualizar todos os produtos
@app.route('/view_products')
def view_products():
    products = Product.query.all()
    return render_template('products/view_products.html', products=products)


# Executando o ambiente
if __name__ == '__main__':
    app.run(debug=True)
    db.create_all()
