import json
from crrud import read_all_pokemon, read_pokemon_by_id, read_pokemon_by_dex_number, read_pokemon_by_name, read_pokemon_by_name, read_pokemon_by_type, create_pokemon, update_pokemon, delete_pokemon
from utils import pokemon_to_dict, export_pokemon_to_json

def print_pokemon(pokemon):
    print(json.dumps(pokemon_to_dict(pokemon)) if pokemon is not None else "No Pokemon found")

def print_menu():
    menu_body = """
---------------------------------
1. Read all Pokemon
2. Read by ID
3. Read by Dex Number
4. Read by Name
5. Read by Type
6. Create a new Pokemon
7. Update a Pokemon
8. Delete a Pokemon
9. Export all Pokemon to JSON
0. Exit
=================================
"""
    print(menu_body)

def menu_logic(flag: bool):
    match(int(input("Enter a choice: "))):
        case 1:
            for pokemon in read_all_pokemon(): print_pokemon(pokemon)
            pass
        case 2:
            id = input("Enter the ID of the Pokemon you want to see: ")
            print_pokemon(read_pokemon_by_id(id))
            pass
        case 3:
            dex_number = input("Enter the Dex Number of the Pokemon you want to see: ")
            print_pokemon(read_pokemon_by_dex_number(dex_number))
            pass
        case 4:
            name = input("Enter the name of the Pokemon you want to see: ")
            print_pokemon(read_pokemon_by_name(name))
            pass
        case 5:
            type_name = input("Enter the type of the Pokemon you want to see: ")
            for pokemon in read_pokemon_by_type(type_name): print_pokemon(pokemon)
            pass
        case 6:
            treecko_json = json.dumps({"dex_number": 999, "name": "Treecko", "type_one": "poison", "generation": 3})
            print(treecko_json)
            confirm = input("Confirm whether you like to create the Pokemon shown above (Y/N): ")
            if confirm.upper() == "Y":
                create_pokemon(treecko_json)
            pass
        case 7:
            id = input("Enter the ID of the Pokemon you want to update: ")
            updates_json = input("Enter the JSON changes you want to make: ")
            update_pokemon(id, updates_json)
            pass
        case 8:
            delete_pokemon()
            pass
        case 9:
            export_pokemon_to_json(read_all_pokemon())
            pass
        case 0:
            print("Bye!")
            flag = False
            pass
    return flag

if __name__ == "__main__":
    running = True
    while running:
        print_menu()
        running = menu_logic(running)
