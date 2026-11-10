import os
from datetime import datetime
from flask import Flask, render_template, redirect, url_for, request, flash
from flask_login import LoginManager, login_user, logout_user, login_required, current_user
from models import db, Usuario, Cliente, OrdemServico
from forms import validar_cliente, validar_os

app = Flask(__name__)
app.config['SECRET_KEY'] = os.environ.get('SECRET_KEY', 'chave-dev-vidracaria-2026')

# Configuração do PostgreSQL (ou SQLite para ambiente local/testes)
db_uri = os.environ.get('DATABASE_URL', 'sqlite:///vidracaria.db')
if db_uri.startswith("postgres://"):
    db_uri = db_uri.replace("postgres://", "postgresql://", 1)
app.config['SQLALCHEMY_DATABASE_URI'] = db_uri
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db.init_app(app)

login_manager = LoginManager()
login_manager.init_app(app)
login_manager.login_view = 'login'

@login_manager.user_loader
def load_user(user_id):
    return db.session.get(Usuario, int(user_id))

# --- ROTAS ---

@app.route('/')
def index():
    if current_user.is_authenticated:
        return redirect(url_for('painel'))
    return redirect(url_for('login'))

@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        email = request.form.get('email')
        senha = request.form.get('senha')
        usuario = Usuario.query.filter_by(email=email).first()
        
        if usuario and usuario.verificar_senha(senha) and usuario.ativo:
            login_user(usuario)
            return redirect(url_for('painel'))
        
        flash('E-mail ou senha incorretos, ou usuário inativo.', 'danger')
    return render_template('login.html')

@app.route('/logout')
@login_required
def logout():
    logout_user()
    flash('Sessão encerrada com sucesso.', 'info')
    return redirect(url_for('login'))

@app.route('/painel')
@login_required
def painel():
    ordens = OrdemServico.query.order_by(OrdemServico.id_os.desc()).all()
    total_ativas = sum(1 for os_item in ordens if os_item.status in ['Aberta', 'Em Andamento'])
    em_andamento = sum(1 for os_item in ordens if os_item.status == 'Em Andamento')
    concluidas = sum(1 for os_item in ordens if os_item.status == 'Concluída')
    
    return render_template('painel.html', 
                           ordens=ordens, 
                           total_ativas=total_ativas, 
                           em_andamento=em_andamento, 
                           concluidas=concluidas)

@app.route('/ordem/nova', methods=['GET', 'POST'])
@login_required
def nova_os():
    if request.method == 'POST':
        nome_cliente = request.form.get('nome_cliente')
        telefone_cliente = request.form.get('telefone_cliente')
        email_cliente = request.form.get('email_cliente')
        descricao = request.form.get('descricao')
        prazo_str = request.form.get('prazo_entrega')
        prioridade = request.form.get('prioridade')

        erros_c = validar_cliente(nome_cliente, telefone_cliente)
        erros_os = validar_os(descricao, prazo_str, prioridade)
        todos_erros = erros_c + erros_os

        if todos_erros:
            for erro in todos_erros:
                flash(erro, 'danger')
            return render_template('nova_os.html')

        # Buscar ou criar cliente
        cliente = Cliente.query.filter_by(telefone=telefone_cliente).first()
        if not cliente:
            cliente = Cliente(nome=nome_cliente, telefone=telefone_cliente, email=email_cliente)
            db.session.add(cliente)
            db.session.flush()

        prazo_dt = datetime.strptime(prazo_str, '%Y-%m-%d').date()
        nova_ordem = OrdemServico(
            descricao=descricao,
            prazo_entrega=prazo_dt,
            prioridade=prioridade,
            status='Aberta',
            cliente_id=cliente.id_cliente,
            usuario_id=current_user.id_usuario
        )
        db.session.add(nova_ordem)
        db.session.commit()

        flash('Ordem de Serviço cadastrada com sucesso!', 'success')
        return redirect(url_for('painel'))

    return render_template('nova_os.html')

@app.route('/ordem/<int:id_os>/status', methods=['POST'])
@login_required
def atualizar_status(id_os):
    ordem = db.session.get(OrdemServico, id_os)
    if ordem:
        novo_status = request.form.get('status')
        if novo_status in ['Aberta', 'Em Andamento', 'Concluída', 'Cancelada']:
            ordem.status = novo_status
            db.session.commit()
            flash(f'Status da OS #{ordem.id_os} atualizado para {novo_status}.', 'success')
    return redirect(url_for('painel'))

@app.route('/ajuda', methods=['GET', 'POST'])

def ajuda():
    if request.method == 'POST':
        # Lógica de recebimento do formulário de ajuda
        flash('Mensagem enviada com sucesso para a gestão!', 'success')
        return render_template('ajuda.html', enviado=True)
    return render_template('ajuda.html')

if __name__ == '__main__':
    with app.app_context():
        db.create_all()
        # Criar usuário inicial para demonstração
        if not Usuario.query.filter_by(email='gerente@vidracaria.com.br').first():
            gerente = Usuario(nome='Fabio Kenji', email='gerente@vidracaria.com.br', perfil='Gerente', ativo=True)
            gerente.set_senha('123456')
            db.session.add(gerente)
            db.session.commit()
    app.run(debug=True)

    