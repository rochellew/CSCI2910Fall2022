from sqlalchemy import Column, Integer, String, Boolean
# this is inheritance-based
from sqlalchemy.ext.declarative import declarative_base

# Base class for the class definitions
Base = declarative_base()

# Note that AnimeCharacter inherits from declarative_base
# via the Base reference object
class AnimeCharacter(Base):
    __tablename__ = "anime_characters" # here we define table name explicitly

    # Class attributes will map to columns in the db
    id = Column(Integer, primary_key=True, autoincrement=True)
    name = Column(String, nullable=False)
    tier = Column(String, nullable=False)
    is_alive = Column(Boolean, nullable=False)
    signature_ability = Column(String)

    # This is similar to C#'s ToString() method
    def __repr__(self):
        return (f"AnimeCharacter(id={self.id!r}, name={self.name!r}, tier={self.tier!r}, is_alive={self.is_alive!r}, signature_ability{self.signature_ability!r})")