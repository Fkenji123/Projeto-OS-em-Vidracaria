from flask_sqlalchemy import SQLAlchemy
from flask_login import UserMixin
from werkzeug.security import generate_password_hash, check_password_hash

db = SQLAlchemy()

class Usuario(UserMixin, db.Model):
    __tablename__ = 'usuario'
    id_usuario = db.Column(db.Integer, primary_key=True)
    nome = db.Column(db.String(120), nullable=False)
    email = db.Column(db.String(150), unique=True, nullable=False)
    senha_hash = db.Column(db.String(255), nullable=False)
    perfil = db.Column(db.String(20), nullable=False)  # Gerente, Atendente, Executor
    ativo = db.Column(db.Boolean, default=True, nullable=False)

    def set_senha(self, senha):
        # Hash seguro com PBKDF2-SHA256 (RNF01)
        self.senha_hash = generate_password_hash(senha)

    def verificar_senha(self, senha):
        return check_password_hash(self.senha_hash, senha)

    def get_id(self):
        return str(self.id_usuario)

class Cliente(db.Model):
    __tablename__ = 'cliente'
    id_cliente = db.Column(db.Integer, primary_key=True)
    nome = db.Column(db.String(120), nullable=False)
    telefone = db.Column(db.String(20), nullable=False)
    email = db.Column(db.String(150), nullable=True)
    
    # Relacionamento 1:N com Ordem de Serviço
    ordens = db.relationship('OrdemServico', backref='cliente', lazy=True)

class OrdemServico(db.Model):
    __tablename__ = 'ordem_servico'
    id_os = db.Column(db.Integer, primary_key=True)
    descricao = db.Column(db.Text, nullable=False)
    prazo_entrega = db.Column(db.Date, nullable=False)
    prioridade = db.Column(db.String(20), nullable=False)  # Baixa, Média, Alta, Urgente
    status = db.Column(db.String(20), default='Aberta', nullable=False)  # Aberta, Em Andamento, Concluída, Cancelada
    
    # Chaves estrangeiras
    cliente_id = db.Column(db.Integer, db.ForeignKey('cliente.id_cliente'), nullable=False)
    usuario_id = db.Column(db.Integer, db.ForeignKey('usuario.id_usuario'), nullable=False)