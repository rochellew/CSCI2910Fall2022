from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from tabulate import tabulate # optional

from db_model import AnimeCharacter, Base

SQLALCHEMY_DB_URL = 'sqlite:///./data.db'
engine = create_engine(SQLALCHEMY_DB_URL)

Base.metadata.create_all(bind=engine)
Session = sessionmaker(bind=engine)

def read_all_characters():
    session = Session()
    return session.query(AnimeCharacter).all()

def display_characters(all_characters):
    table = []
    table.append(["Id", "Name", "Tier", "Status", "Signature Ability"])

    for character in all_characters:
        table.append([character.id, character.name, character.tier, character.is_alive, character.signature_ability])

    print(tabulate(table, headers='firstrow', tablefmt='fancy-grid'))

def add_character():
    session = Session()
    input_name = input("What is the character's name: ")

    tiers = ['S', 'A', 'B', 'C', 'D', 'F']
    input_tier = input("What is the character's tier: ")
    while input_tier not in tiers:
        input_tier = input("Invalid. What is the character's tier: ")

    input_status = input("Is the character alive (Y/N): ").upper()
    while input_status not in ["Y", "N"]:
        input_status = input("Is the character alive (Y/N): ").upper()
    if input_status == "Y":
        input_status = True
    else:
        input_status = False

    input_ability = input("What is the character's signature ability: ")

    # create character 
    character = AnimeCharacter(name=input_name, 
                               tier=input_tier,
                               is_alive=input_status, 
                               signature_ability = input_ability)
    
    session.add(character)
    session.commit()
    session.close()

add_character()
display_characters(read_all_characters())