import json
import readchar

from data_model import Pokemon

def pokemon_to_dict(pokemon: Pokemon) -> dict:
    return {
        "Id": pokemon.id,
        "DexNumber": pokemon.dex_number,
        "Name": pokemon.name,
        "Type1": pokemon.type_one,
        "Type2": pokemon.type_two,
        "Generation": pokemon.generation,
    }

def export_pokemon_to_json(data: Pokemon | list[Pokemon], filepath: str | None = None) -> None:
    if isinstance(data, list):
        payload = [pokemon_to_dict(pokemon) for pokemon in data]
        count = len(payload)
    else:
        payload = pokemon_to_dict(data)
        count = 1

    exported_json = json.dumps(payload, indent=2)

    if filepath is None:
        print(exported_json)
        print(f"Exported {count} record(s) to console")
    else:
        with open(filepath, "w") as f:
            f.write(exported_json)
        print(f"Exported {count} record(s) to {filepath}")

def read_line_or_cancel(prompt: str) -> str | None:
    print(prompt, end="", flush=True)
    buffer=""
    while True:
        key = readchar.readkey()
        if key == readchar.key.ESC:
            print()
            return None
        if key == readchar.key.ENTER:
            print()
            return buffer
        if key == readchar.key.BACKSPACE:
            buffer = buffer[:-1]
            print("\b \b", end="", flush=True)
        else:
            buffer += key
            print(key, end="", flush=True)    
