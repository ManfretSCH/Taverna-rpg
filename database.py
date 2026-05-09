from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, declarative_base

DATABASE_URL =  "sqlite:///./McGustavo.db"

engine = create_engine(DATABASE_URL, echo=True)

base = declarative_base()

sessionLocal = sessionmaker(
    autocommit=False,
    autoflush=False,
    bind=engine
)

