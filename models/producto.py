from database import Base
from sqlalchemy import String
from sqlalchemy.orm import Mapped, mapped_column

class Producto(Base):
    __tablename__ = 'productos'

    id: Mapped[int] = mapped_column(primary_key=True, autoincrement=True)
    nombre: Mapped[str] = mapped_column(String(30))
    categoria: Mapped[str]
    precio : Mapped[float]
    disponible: Mapped[bool] = mapped_column(default=True)

