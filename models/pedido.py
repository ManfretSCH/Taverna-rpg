from datetime import datetime
from database import base
from models.cliente import Cliente
from models.detalle_pedido import DetallePedido
from sqlalchemy import ForeignKey
from sqlalchemy.orm import Mapped, mapped_column, relationship

class Pedido(base):
    __tablename__ = 'pedidos'


    id: Mapped[int] = mapped_column(primary_key=True, autoincrement=True)
    cliente_id: Mapped[int] = mapped_column(ForeignKey('clientes.id'))
    fecha: Mapped[datetime] = mapped_column(default=datetime.now)
    total: Mapped[float]
    estado: Mapped[str]
    cliente: Mapped['Cliente'] = relationship(back_populates='pedidos')
    detalles: Mapped[list["DetallePedido"]] = relationship(back_populates="pedido", cascade="all, delete-orphan")
