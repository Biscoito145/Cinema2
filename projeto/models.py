from projeto import database, login_manager
from datetime import datetime
from flask_login import UserMixin


@login_manager.user_loader
def load_usuario(id_usuario):
    return Usuario.query.get(int(id_usuario))


class Usuario(database.Model, UserMixin):
    id = database.Column(database.Integer, primary_key=True)
    username = database.Column(database.String, nullable=False)
    email = database.Column(database.String, nullable=False, unique=True)
    senha = database.Column(database.String, nullable=False)
    foto_perfil = database.Column(database.String, nullable=False, default='default.png')
    posts = database.relationship('Post', backref='autor', lazy=True)
    cartao = database.relationship('Cartao', backref='titular', lazy=True)
    cursos = database.Column(database.String, nullable=False, default='Não Informado')

    def contar_posts(self):
        return len(self.posts)


class Post(database.Model):
    id = database.Column(database.Integer, primary_key=True)
    titulo = database.Column(database.String, nullable=False)
    corpo = database.Column(database.Text, nullable=False)
    arquivo = database.Column(database.String)
    data_criacao = database.Column(database.DateTime, nullable=False, default=datetime.utcnow)
    id_usuario = database.Column(database.Integer, database.ForeignKey('usuario.id'), nullable=False)


class Cartao(database.Model):
    id = database.Column(database.Integer, primary_key=True)
    numero_cartao = database.Column(database.String, nullable=False)
    data_expiracao= database.Column(database.String, nullable=False)
    cod = database.Column(database.String, nullable=False)
    nome_titular = database.Column(database.String, nullable=False)
    id_titular = database.Column(database.Integer, database.ForeignKey('usuario.id'), nullable=False)
