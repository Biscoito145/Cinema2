from projeto import app
from projeto.models import Post
from flask import url_for
from pathlib import Path

app.config['SERVER_NAME'] = 'localhost:5000'  # Altere para o seu nome de servidor
app.config['APPLICATION_ROOT'] = '/'  # Se necessário
app.config['PREFERRED_URL_SCHEME'] = 'http'  # Ou 'https', dependendo do seu ambiente


with app.app_context():
    for post in Post.query.all():
        print(url_for('static', filename='post_file/' + post.arquivo))
        print(post.arquivo)
        break

#     database.create_all()
    # usuario1 = Usuario(username='Calabreso123', email='calabreso@gmail.com', senha='123456')
    # usuario2 = Usuario(username='Ludmillo123', email='ludmillo@gmail.com', senha='123456')
    # database.session.add(usuario1)
    # database.session.add(usuario2)
    # database.session.commit()
    # user = Usuario.query.first()
    # print(user.senha)
    # usuario_teste = Usuario.query.first()
    # print(usuario_teste.email)
    # user = Usuario.query.filter_by(email='arabiosaudito@gmail.com').first()
    # print(user.senha)
    # usuario2 = Usuario.query.filter_by(email='ludmillo@gmail.com').first()
    # print(usuario_teste.foto_perfil)
    # print(usuario2.id)
    #
    # post1 = Post(titulo='Fist Post', corpo='This is my firs post in this social midia, motherfuckers', id_usuario=1)
    # database.session.add(post1)
    # database.session.commit()
    #
    # print(Post.query.all())
    # post = Post.query.first()
    # print(post.corpo)
    # print(post.autor)
    # autor_post = post.autor
    # print(autor_post.username)


import os
from pathlib import Path
#
# caminho = os.getcwd()
# pasta = os.listdir("templates")
# for nome in pasta:
#     if nome == "filmes":
#         lista_filmes = os.listdir(nome)
#         print(lista_filmes)
# lista_filmes = os.listdir("templates/filmes")
# print(lista_filmes)
#
# caminho = Path(app.root_path) / Path("static/filmes")
# print('-'*50)
# print(caminho)
# caminho = os.getcwd() + (r"\templates\filmes")
# print(caminho2)
#
# lista_filmes = [file for file in os.listdir(caminho)]
#
# for nome in lista_filmes:
#     print(nome)
#
# print(lista_filmes)
# print(os.listdir(caminho))

#
# from pydrive.auth import GoogleAuth
# from pydrive.drive import GoogleDrive
#
# gauth = GoogleAuth()
# gauth.LocalWebserverAuth()
# #
# drive = GoogleDrive(gauth)
#
# folder_id = '1TVN33BiN1Qtszo3uROwM0QMVnQ5qBz_D'
# file_list = drive.ListFile({'q': f"'{folder_id}' in parents and trashed=false"}).GetList()
#
# video_urls = [file['webContentLink'] for file in file_list if file['mimeType'].startswith('video/')]
#
# # Agora você pode usar os URLs dos vídeos em seu código
# for url in video_urls:
#     print(url)

# with app.app_context():
#     user = Usuario.query.filter_by(email="ludmillo@gmail.com").first()
#     print(user.cursos)

# from pydrive.auth import GoogleAuth
# from pydrive.drive import GoogleDrive
#
#
# gauth = GoogleAuth()
# gauth.LocalWebserverAuth()
#
# drive = GoogleDrive(gauth)
#
# folder_id = '1TVN33BiN1Qtszo3uROwM0QMVnQ5qBz_D'
# file_list = drive.ListFile({'q': f"'{folder_id}' in parents and trashed=false"}).GetList()
#
# video_urls = [file['webContentLink'] for file in file_list if file['mimeType'].startswith('video/')]
# with app.app_context():
#     lista_objetos_usuario = Usuario.query.all()
#     lista_usuarios = [usuario.username for usuario in lista_objetos_usuario]
#     print(lista_usuarios)

# from unidecode import unidecode
# curso = "Ação;Comédia;Ficção Científica"
# lista_generos = curso.split(";")
# formatados = [unidecode(curso).casefold().replace(" ", "") for curso in lista_generos]
# print(lista_generos)
# print(formatados)
# # cursos_formatados = [unidecode(curso).casefold().replace(" ", "") for curso in current_user.cursos]


# string = "Ação;Comédia;Romance;Ficcão Cíentíifica"
# lista = string.split(";")
# print(lista)

    # database.create_all()
    # posts = Post.query.all()
    # for post in posts:

