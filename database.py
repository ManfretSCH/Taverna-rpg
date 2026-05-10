from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, DeclarativeBase

DATABASE_URL =  "sqlite:///./McGustavo.db"

engine = create_engine(DATABASE_URL, echo=True)

class Base(DeclarativeBase):
    pass

sessionLocal = sessionmaker(
    autocommit=False,
    autoflush=False,
    bind=engine
)

