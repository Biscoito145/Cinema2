from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField, BooleanField, TextAreaField, DateField, IntegerField, SelectField
from wtforms.validators import DataRequired, Length, Email, EqualTo, ValidationError
from projeto.models import Usuario
from flask_login import current_user
from flask_wtf.file import FileField, FileAllowed
from werkzeug.utils import secure_filename
from pathlib import Path
from projeto import app
from datetime import datetime


class FormCriarConta(FlaskForm):
    username = StringField("Nome de Usuário", validators=[DataRequired()])
    email = StringField("E-mail", validators=[DataRequired(), Email()])
    senha = PasswordField("Senha", validators=[DataRequired(), Length(6, 20)])
    confirmacao_senha = PasswordField("Confirmação da Senha", validators=[DataRequired(), EqualTo("senha")])
    botao_submit_criarconta = SubmitField("Criar Conta")

    def validate_email(self, email):
        usuario = Usuario.query.filter_by(email=email.data).first()
        if usuario:
            raise ValidationError("E-mail já cadastrado, insira outro e-mail para criar uma conta")


class FormLogin(FlaskForm):
    email = StringField("E-mail", validators=[DataRequired(), Email()])
    senha = PasswordField("Senha", validators=[DataRequired(), Length(6, 20)])
    lembrar_dados = BooleanField("Lembrar Dados de Acesso")
    botao_submit_login = SubmitField("Fazer Login")


class FormEditarPerfil(FlaskForm):
    username = StringField("Nome de Usuário", validators=[DataRequired()])
    email = StringField("E-mail", validators=[DataRequired(), Email()])
    foto_perfil = FileField("Atualizar Foto de Perfil", validators=[FileAllowed(["jpg", "png"])])
    genero_acao = BooleanField("Ação")
    genero_comedia = BooleanField("Comédia")
    genero_terror = BooleanField("Terror")
    genero_suspense = BooleanField("Suspense")
    genero_drama = BooleanField("Drama")
    genero_romance = BooleanField("Romance")
    genero_ficcaocientifica = BooleanField("Ficção Científica")
    genero_animacao = BooleanField("Animação")

    botao_submit_editarperfil = SubmitField("Confirmar Edição")

    def validate_email(self, email):
        if current_user.email != email.data:
            usuario = Usuario.query.filter_by(email=email.data).first()
            if usuario:
                raise ValidationError("Já existe um usuário com esse e-mail. Cadastre outro e-mail")


class FormCriarPost(FlaskForm):
    titulo = StringField("Título do Post", validators=[DataRequired(), Length(2, 200)])
    corpo = TextAreaField("Corpo do Post", validators=[DataRequired()])
    arquivo = FileField("Selecione um arquivo", validators=[FileAllowed(["jpg", "png", "mp4"])])
    botao_submit = SubmitField("Criar Post")


class FormPagamento(FlaskForm):
    numero_cartao = StringField("Número do Cartão", validators=[DataRequired(), Length(13,15)])

    meses = ['01', '02', '03', '04', '05', '06', '07', '08', '09', '10', '11', '12']
    data_expiracao = SelectField("Mês de Validade do Cartão",choices=meses, validators=[DataRequired()])

    data_completa = datetime.now
    ano = data_completa().strftime("%Y")
    anos = [i for i in range(int(ano), int(ano) + 6)]
    ano_expiracao = SelectField("Ano de Validade do Cartão",choices=anos, validators=[DataRequired()])

    cod_seguranca = StringField("Código de Segurança do Cartão", validators=[DataRequired(), Length(3,4)])

    nome_cartao = StringField("Nome do Titular", validators=[DataRequired()])

    botao_submit = SubmitField("Salvar Dados")

    def validate_numero_cartao(self, field):
        if not field.data.isnumeric():
            raise ValidationError("Somente números, seu Animal!.")


    def validate_cod_seguranca(self, field):
        if not field.data.isnumeric():
            raise ValidationError("Tu és lesa ou só te fazes? Apenas Números, seu Imbecil!")


    def validate_nome_cartao(self, field):
        field = field.data.casefold().strip().replace(" ", "")
        if not field.isalpha():
            raise ValidationError("O campo não pode conter números, que lixo de aberração você é?.")


