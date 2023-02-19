from sqlalchemy.orm import declarative_base, Session
from sqlalchemy.orm import relationship
from sqlalchemy import Column, create_engine, inspect, select, func
from sqlalchemy import Integer
from sqlalchemy import String
from sqlalchemy import ForeignKey
from sqlalchemy import BINARY
from sqlalchemy import DECIMAL

Base = declarative_base()


class Cliente(Base):
    __tablename__ = "cliente"
    id = Column(Integer, primary_key=True)
    nome = Column(String)
    cpf = Column(String(9))
    endereco = Column(String(9))

    conta = relationship(
        "Conta", back_populates="cliente", cascade="all, delete-orphan"
    )

    def __repr__(self):
        return f"Cliente(id={self.id}, nome={self.nome}, cpf={self.cpf}, endereco={self.endereco})"


class Conta(Base):
    __tablename__ = "conta"
    id = Column(BINARY, primary_key=True)
    tipo = Column(String)
    agencia = Column(String(9))
    num = Column(Integer)
    id_cliente = Column(Integer, ForeignKey("cliente.id"))
    saldo = Column(DECIMAL)

    cliente = relationship(
        "Cliente", back_populates="conta"
    )

    def __repr__(self):
        return f"Conta(id={self.id}, tipo={self.tipo}, agencia={self.agencia}, num={self.num}, saldo={self.saldo})"


print(Cliente.__tablename__)
print(Conta.__tablename__)

engine = create_engine("sqlite://")

Base.metadata.create_all(engine)

inspetor_engine = inspect(engine)

print(inspetor_engine.has_table("cliente"))
print(inspetor_engine.get_table_names())
print(inspetor_engine.default_schema_name)

with Session(engine) as session:
    andre = Cliente(
        nome='andre',
        cpf='123123123',
        endereco='rua ana',
        conta=[Conta(
            id=b'1',
            tipo='corrente',
            agencia='21.2-09',
            num='12',
            saldo='150'
        )]
    )
    filipe = Cliente(
        nome='filipe',
        cpf='654654656',
        endereco='rua ida',
        conta=[Conta(
            id=b'0',
            tipo='poupanca',
            agencia='23.2-23',
            num='13',
            saldo='300'
        )]
    )

    session.add_all([andre, filipe])
    session.commit()

    stmt = select(Cliente).where(Cliente.nome.in_(['filipe']))
    print('recuperando usuário')
    for user in session.scalars(stmt):
        print(user)

    stmt_conta = select(Conta).where(Conta.id_cliente.in_([2]))
    print('recuperando conta')
    for user in session.scalars(stmt_conta):
        print(user)
