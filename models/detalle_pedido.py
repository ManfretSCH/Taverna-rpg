from database import base
from sqlalchemy import ForeignKey
from sqlalchemy.orm import Mapped, mapped_column, relationship

class DetallePedido(base):
    __tablename__ = 'detallePedidos'

    pedido_id: Mapped[int] = mapped_column(ForeignKey('pedidos.id'))
    producto_id: Mapped[int] = mapped_column(ForeignKey('producto.id'))
    cantidad: Mapped[int]
    subtotal: Mapped[float]
    pedido: Mapped['Pedido'] = relationship(back_populates='detalles')