from projeto import app, database
from projeto.models import Post, Cartao
from flask import url_for
from pathlib import Path
import os
import secrets
from werkzeug.utils import secure_filename


app.config['SERVER_NAME'] = 'localhost:5000'  # Altere para o seu nome de servidor
app.config['APPLICATION_ROOT'] = '/'  # Se necessário
app.config['PREFERRED_URL_SCHEME'] = 'http'  # Ou 'https', dependendo do seu ambiente

from datetime import datetime
with app.app_context():
    # database.drop_all()
    # database.create_all()
    print(Cartao.query.first().numero_cartao)
    # mes = '01'
    # ano = 2022
    # data = f"{str(mes)}/{str(ano)}"
    # print(data)

    # nome = '              Ren a '
    # nome = nome.casefold().strip().replace(' ', '')
    # if nome.isalpha():
    #     print('sim')
    # else:
    #     print('n')
    # print(nome)

    # database.drop_all()
    # datetime.strftime(datetime.now(), "%Y")
    # print( datetime.strftime(datetime.now(), "%Y"))
    # database.create_all()
    # print(Cartao.query.first().nome_titular)
    # field = "MAjekdcskln 22 2  cw22"
    # field = field.casefold().strip().replace(" ", "")
    # if field.isalpha():
    #     print(field)
    #     print("O campo não pode conter números, que lixo de aberração você é?.")
    # else:
    #     print("tudo certo pwai")
    # # nome_seguro = 'banana'
    # print(Post.query.all())
    # print(Cartao.query.all())
    # print((Path(app.root_path) / Path("static/post_file") / Path(nome_seguro)))
    # for post in Post.query.all():
    #     print(url_for('static', filename='post_file/' + post.arquivo))
    #     print(post.arquivo)
    #     break
    # arquivo = 'hyedsbhjvdhbhfsbkdwkjsfchkdsyuief.mp4'
    # data = datetime.utcnow
    # print(data().strftime("%d/%m/%Y"))
    # # data = data.strftime("Y")
    # print(data)
    # for i in range(int(data), int(data) + 6):
    #     print(i)
    # extensao = arquivo[-4:]
    # print(extensao)
    # cod = secrets.token_hex(8)
    # arquivo = arquivo[:-4] + cod + extensao
    # print(arquivo)
    # pasta_filmes = Path(app.root_path) / Path("static/filmes")
    # lista_filmes = os.listdir(pasta_filmes)
    # lista_filmes = [filme[:-4] for filme in lista_filmes]
    # print(lista_filmes)
    # nome_seguro = secure_filename(arquivo.filename)
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

