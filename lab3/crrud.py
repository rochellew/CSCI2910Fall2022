import json

from sqlalchemy import create_engine, select, or_
from sqlalchemy.orm import sessionmaker

from data_model import Pokemon, Base
from utils import read_line_or_cancel, pokemon_to_dict

CONNECTION_STRING = "sqlite:///./lab_data.db"
engine = create_engine(CONNECTION_STRING)

Base.metadata.create_all(bind=engine)

Session = sessionmaker(bind=engine)

def create_pokemon(create_json:str):
    create = json.loads(create_json)
    pokemon = Pokemon(**create)
    with Session() as session:
        session.add(pokemon)
        session.commit()
        print(f"Created: {json.dumps(pokemon_to_dict(pokemon))}")

def read_pokemon_by_id(id: int):
    with Session() as session:
        statement = select(Pokemon).filter_by(id = id)
        return session.scalars(statement).one_or_none()

def read_pokemon_by_dex_number(dex_number: int):
    with Session() as session:
        statement = select(Pokemon).filter_by(dex_number = dex_number)
        return session.scalars(statement).one_or_none()
    
def read_pokemon_by_name(name:str):
    with Session() as session:
        statement = select(Pokemon).filter_by(name = name.capitalize())
        return session.scalars(statement).one_or_none()

def read_pokemon_by_type(type_name: str):
    with Session() as session:
        statement = select(Pokemon).where(or_(Pokemon.type_one == type_name.capitalize(), Pokemon.type_two == type_name.capitalize()))
        return session.scalars(statement).all()

def read_all_pokemon():
    with Session() as session:
        return session.scalars(select(Pokemon)).all()

def update_pokemon(id: int, updates_json: str):
    updates = json.loads(updates_json)
    with Session() as session:
        statement = select(Pokemon).filter_by(id = id)
        pokemon = session.scalars(statement).one_or_none()
        if pokemon is None:
            print(f"No Pokemon found with ID = {id}")
            return
        for key, value in updates.items():
            setattr(pokemon, key, value)
        session.commit()
        print(f"Updated: {json.dumps(pokemon_to_dict(pokemon))}")

def delete_pokemon():
    name = read_line_or_cancel("Enter the name of the pokemon you want to delete (esc to cancel): ")
    if name is None:
        print("DELETE operation cancelled...")
        return

    with Session() as session:
        statement = select(Pokemon).filter_by(name = name.capitalize())
        pokemon_to_delete = session.scalars(statement).one_or_none()

        if pokemon_to_delete is None:
            print(f"No Pokemon found with name = {name}")
            return

        if input(f"Confirming DELETE on {name} (Y/N): ").upper() == "Y":
            session.delete(pokemon_to_delete)
            session.commit()
            print(f"Deleted: {json.dumps(pokemon_to_dict(pokemon_to_delete))}")
        else:
            print("DELETE operation cancelled...")
