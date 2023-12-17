from projeto import app, database, bcrypt
from flask import render_template, flash, url_for, redirect, request, abort
from projeto.forms import FormCriarConta, FormLogin, FormEditarPerfil, FormCriarPost, FormPagamento
from projeto.models import Usuario, Post, Cartao
from flask_login import login_user, logout_user, current_user, login_required
import os
from pathlib import Path
import secrets
from PIL import Image
from unidecode import unidecode
from werkzeug.utils import secure_filename


@app.route("/")
def home():
    posts = Post.query.order_by(Post.id.desc())
    return render_template("homepage.html", posts=posts)


@app.route("/contato")
def contato():
    return render_template("contato.html")


@app.route("/filmes")
@login_required
def filmes():
    caminho = Path(app.root_path) / Path("static/filmes")
    lista_filmes = os.listdir(caminho)
    return render_template("filmes.html", lista_filmes=lista_filmes)


@app.route("/login", methods=["GET", "POST"])
def login():
    form_login = FormLogin()
    form_criarconta = FormCriarConta()

    if form_login.validate_on_submit() and "botao_submit_login" in request.form:
        usuario = Usuario.query.filter_by(email=form_login.email.data).first()
        if usuario and bcrypt.check_password_hash(usuario.senha, form_login.senha.data):
            login_user(usuario, remember=form_login.lembrar_dados.data)
            flash(f"Login realizado com sucesso no e-mail: {form_login.email.data}", "alert-success")
            par_next = request.args.get("next")
            if par_next:
                return redirect(par_next)
            else:
                return redirect(url_for("home"))
        else:
            flash("Falha no Login, E-mail ou Senha Incorretos. Tente Novamente", "alert-danger")
    if form_criarconta.validate_on_submit():
        senha_criptografa = bcrypt.generate_password_hash(form_criarconta.senha.data)
        usuario = Usuario(username=form_criarconta.username.data, email=form_criarconta.email.data,
                          senha=senha_criptografa)
        database.session.add(usuario)
        database.session.commit()
        flash(f"Conta criada com sucesso no e-mail: {form_criarconta.email.data}", "alert-success")
        return redirect(url_for("home"))

    return render_template("login.html", form_login=form_login, form_criarconta=form_criarconta)


@app.route("/sair")
@login_required
def sair():
    logout_user()
    flash("Logout Feito com Sucesso", "alert-success")
    return redirect(url_for("home"))


@app.route("/perfil")
@login_required
def perfil():
    foto_perfil = url_for("static", filename=f"fotos_perfil/{current_user.foto_perfil}")
    return render_template("perfil.html", foto_perfil=foto_perfil)


@app.route("/post/criar", methods=["GET", "POST"])
@login_required
def criar_post():
    form = FormCriarPost()
    if form.validate_on_submit():
        if form.arquivo.data:
            arquivo = form.arquivo.data
            extensao = arquivo.filename[-4:]
            cod = secrets.token_hex(8)
            arquivo.filename = arquivo.filename[:-4] + cod + extensao
            nome_seguro = secure_filename(arquivo.filename)
            arquivo.save(Path(app.root_path) / Path("static/post_file") / Path(nome_seguro))
            post = Post(titulo=form.titulo.data, corpo=form.corpo.data, autor=current_user, arquivo=nome_seguro)
            database.session.add(post)
            database.session.commit()
        else:
            nome_arquivo_padrao = 'arquivo'
            post = Post(titulo=form.titulo.data, corpo=form.corpo.data, autor=current_user, arquivo=nome_arquivo_padrao)
            database.session.add(post)
            database.session.commit()
        flash("Post Criado com Sucesso", "alert-success")
        return redirect(url_for("home"))
    return render_template("criarpost.html", form=form)


@app.route("/usuarios")
@login_required
def usuarios():
    lista_usuarios = Usuario.query.all()
    return render_template("usuarios.html", lista_usuarios=lista_usuarios)


def salvar_imagem(imagem):
    # adicionar o código na imagem
    cod = secrets.token_hex(8)
    nome, extensao = os.path.splitext(imagem.filename)
    nome_arquivo = nome + cod + extensao
    caminho = Path(app.root_path) / Path("static/fotos_perfil") / Path(nome_arquivo)
    # reduzir a imagem
    tamanho = (200,200)
    imagem_reduzida = Image.open(imagem)
    imagem_reduzida.thumbnail(tamanho)
    # salvar a imagem
    imagem_reduzida.save(caminho)
    return nome_arquivo


def atualizar_filmes(form):
    lista_generos = []
    for campo in form:
        if "genero_" in campo.name:
            if campo.data:
                lista_generos.append(campo.label.text)
    return ";".join(lista_generos)


@app.route("/perfil/editar", methods=["GET", "POST"])
@login_required
def editar_perfil():
    foto_perfil = url_for("static", filename=f"fotos_perfil/{current_user.foto_perfil}")
    form = FormEditarPerfil()
    if form.validate_on_submit():
        current_user.username = form.username.data
        current_user.email = form.email.data
        if form.foto_perfil.data:
            nome_imagem = salvar_imagem(form.foto_perfil.data)
            current_user.foto_perfil = nome_imagem
        current_user.cursos = atualizar_filmes(form)
        database.session.commit()
        flash("Perfil Atualizado com sucesso", "alert-success")
        return redirect(url_for("perfil"))
    elif request.method == 'GET':
        form.username.data = current_user.username
        form.email.data = current_user.email
        for campo in form:
            if "genero_" in campo.name:
                genero_nome = campo.name[7:]
                cursos_formatados = [unidecode(curso).casefold().replace(" ", "") for curso in current_user.cursos.split(";")]
                if genero_nome in cursos_formatados:
                    campo.data = True
    return render_template("editarperfil.html", foto_perfil=foto_perfil, form=form, genero_nome=genero_nome, cursos_formatados=cursos_formatados)


@app.route("/post/<post_id>",  methods=["GET", "POST"])
@login_required
def exibir_post(post_id):
    post = Post.query.get(post_id)
    if current_user == post.autor:
        form = FormCriarPost()
        if request.method == 'GET':
            form.titulo.data = post.titulo
            form.corpo.data = post.corpo
            form.arquivo.data =  post.arquivo
        elif form.validate_on_submit():
            post.titulo = form.titulo.data
            post.corpo = form.corpo.data
            if form.arquivo.data:
                post.arquivo = form.arquivo.data
            else:
                post.arquivo = 'arquivo'
            database.session.commit()
            flash("Post Atualizado Com Sucesso!", "alert-success")
            return redirect(url_for("home"))
    else:
        form = None
    return render_template("post.html", post=post, form=form)


@app.route("/post/<post_id>/excluir",  methods=["GET", "POST"])
@login_required
def excluir_post(post_id):
    post = Post.query.get(post_id)
    if current_user == post.autor:
        database.session.delete(post)
        database.session.commit()
        flash("Post Excluído com Sucesso!", "alert-danger")
        return redirect(url_for("home"))
    else:
        abort(404)


@app.route("/pagamento", methods=["GET", "POST"])
@login_required
def fazer_pagamento():
    form_pagamento = FormPagamento()
    if form_pagamento.validate_on_submit():
        cartao = Cartao(numero_cartao=form_pagamento.numero_cartao.data,
                        data_expiracao=f"{str(form_pagamento.data_expiracao.data)}/{str(form_pagamento.ano_expiracao.data)}",
                        cod=form_pagamento.cod_seguranca.data, nome_titular=form_pagamento.nome_cartao.data, titular=current_user)
        flash("Cartão Salvo com Sucesso!", "alert-success")
        database.session.add(cartao)
        database.session.commit()
        return redirect(url_for("home"))
    return render_template("pagamento.html", form=form_pagamento)




