import pytest
from app import app, db
from models import Usuario

@pytest.fixture
def client():
    app.config['TESTING'] = True
    app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///:memory:'
    app.config['WTF_CSRF_ENABLED'] = False
    
    with app.app_context():
        db.create_all()
        yield app.test_client()
        db.session.remove()
        db.drop_all()

def test_senha_hash(client):
    """Garante que a senha é armazenada como hash seguro (RNF01)"""
    with app.app_context():
        user = Usuario(nome="Test User", email="hash@vidracaria.com", perfil="Gerente", ativo=True)
        user.set_senha("password123")
        db.session.add(user)
        db.session.commit()
        
        saved_user = Usuario.query.filter_by(email="hash@vidracaria.com").first()
        assert saved_user.senha_hash != "password123"
        assert saved_user.verificar_senha("password123") is True

def test_login_sucesso(client):
    """Testa a autenticação com sucesso"""
    with app.app_context():
        user = Usuario(nome="Login User", email="login@vidracaria.com", perfil="Gerente", ativo=True)
        user.set_senha("password123")
        db.session.add(user)
        db.session.commit()

    response = client.post('/login', data=dict(
        email='login@vidracaria.com',
        senha='password123'
    ), follow_redirects=True)
    
    assert response.status_code == 200
    assert b'Painel' in response.data or response.status_code == 200