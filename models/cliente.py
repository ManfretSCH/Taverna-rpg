from database import base
from sqlalchemy import String
from sqlalchemy.orm import Mapped, mapped_column, relationship, Session


class Cliente(base):
    __tablename__ = 'clientes'

    id: Mapped[int] = mapped_column(primary_key=True, autoincrement=True)
    nombre: Mapped[str] = mapped_column(String(30))
    ruc: Mapped[int] = mapped_column(unique=True)
    tel: Mapped[str] = mapped_column(String(20))
    direccion: Mapped[str | None] = mapped_column(String(100), nullable=True)

    # sirve para relacionar pedido.cliente, acceder al cliente atravez del pedido
    pedidos: Mapped[list['Pedido']] = relationship(back_populates='cliente')


class ClienteCRUD:
    def __init__(self, session: Session):
        self.session = session

    def crear(self, nombre, ruc, tel, direccion = None):
        cliente = Cliente(nombre, ruc, tel, direccion)
        self.session.add(cliente)
        self.session.commit()
        return cliente
    
    def listar(self):
        return self.session.query(Cliente).filter(Cliente).all()
    
    def obtener(self, id):
        return self.session.query(Cliente).filter(Cliente.id == id).first()
    
    def modificar(self, id, **datos):
        cliente_db = self.session.get(Cliente, id)

        if cliente_db is None:
            return None
        
        for campo, valor in datos.items():
            setattr(cliente_db, campo, valor)
        
        self.session.commit()
        return cliente_db
    
    def eliminar(self, id):
        cliente_db = self.session.get(Cliente, id)
        if cliente_db:
            self.session.delete(cliente_db)
            self.session.commit()
    

