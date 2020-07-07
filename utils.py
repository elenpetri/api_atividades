from models import Pessoas, Usuarios
from models import Atividades


def insere_pessoas():
    pessoa = Pessoas(nome='Fernanda', idade=27)
    print(pessoa)
    pessoa.save()


def consulta_pessoas():
    pessoas = Pessoas.query.all()
    print(pessoas)
    # for i in pessoa:
    #     print(i.nome)
    pessoa = Pessoas.query.filter_by(nome='Elen').first()
    # # for p in pessoa:
    print(pessoa.idade)

def altera_pessoas():
    pessoa = Pessoas.query.filter_by(nome='Elen').first()
    pessoa.nome = 'Elen'
    pessoa.save()

def exclui_pessoas():
    pessoa = Pessoas.query.filter_by(nome='Fernada').first()
    pessoa.delete()

def insere_usuario(login, senha):
    usuario = Usuarios(login=login, senha=senha)
    usuario.save()

def consulta_todos_usuarios():
    usuarios = Usuarios.query.all()
    print(usuarios)

def exclui_usuarios():
    usuario = Usuarios.query.filter_by(login='felipe').first()
    usuario.delete()

def consulta_atividade():
    atividades = Atividades.query.all()
    print(atividades)

if __name__ == '__main__':
    # insere_usuario('giovanna', '1234')
    # insere_usuario('felipe', '4321')
    # exclui_usuarios()
    consulta_todos_usuarios()
    # insere_pessoas()
    # consulta_atividade()
    # exclui_pessoas()
    # altera_pessoas()


