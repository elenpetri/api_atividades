from models import Pessoas



def insere_pessoas():
    pessoa = Pessoas(nome='Elen', idade=26)
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
    pessoa = Pessoas.query.filter_by(nome='Elen').first()
    pessoa.delete()

if __name__ == '__main__':
    # insere_pessoas()
    consulta_pessoas()
    exclui_pessoas()
    # altera_pessoas()
