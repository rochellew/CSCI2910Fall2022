from sqlalchemy import Column, String, Integer
from sqlalchemy.orm import declarative_base

Base = declarative_base()

class Pokemon(Base):
    __tablename__ = "Pokemon"

    id          = Column("Id", Integer, primary_key=True, auto_increment = True)
    dex_number  = Column("DexNumber", Integer, nullable=False)
    name        = Column("Name", String, nullable=False)
    type_one    = Column("Type1", String, nullable=False)
    type_two    = Column("Type2", String)
    generation  = Column("Generation", Integer, nullable=False)