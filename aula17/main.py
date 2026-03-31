from sqlalchemy import Column, Integer, String, create_engine
from sqlalchemy.orm import declarative_base, sessionmaker

# create a connection to sqllite in memory
engine = create_engine("sqlite:///meubanco.db", echo=True)

print("Conexão estabelecida")


Base = declarative_base()


class Usuarios(Base):
    __tablename__ = "usuarios"

    id = Column(Integer, primary_key=True)
    nome = Column(String)
    idade = Column(Integer)


Base.metadata.create_all(engine)

Session = sessionmaker(bind=engine)
session = Session()

novo_usuario = Usuarios(nome="João", idade=28)
session.add(novo_usuario)
session.commit()

print(f"Usuário inserido com sucesso")

usuario = session.query(Usuarios).filter_by(nome="João").first()

print(f"Usuário encontrado: {usuario.nome}, idade: {usuario.idade}")

try:
    novo_usuario = Usuarios(nome="Ana", idade=25)
    session.add(novo_usuario)
    session.commit()
except ValueError as e:
    session.rollback()
    raise print(f"Erro de transação: {e}")
finally:
    session.close()

Session = sessionmaker(bind=engine)

with Session() as session, session.begin():
    novo_usuario2 = Usuarios(nome="Pedrinho", idade=17)
    session.add(novo_usuario2)
    # session.commit()
    # the libe above is needed when we dont use the command "session.begin()"
    print(f"Usuário Pedrinho adicionado")
    # O commit é feito automaticamente aqui, se não houver exceções
    # O rollback é automaticamente chamado se uma exceção ocorrer
    # A sessão é fechada automaticamente ao sair do bloco with
