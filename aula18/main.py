import json

import requests as re
from pydantic import BaseModel, ConfigDict


class PokemonSchema(BaseModel):
    name: str
    types: str
    model_config = ConfigDict(from_attributes=True)


def pegar_pokemom(id: int) -> PokemonSchema:
    response = re.get(f"https://pokeapi.co/api/v2/pokemon/{id}")

    response_json = response.json()

    with open("aula18/json.json", "w") as file:
        file.write(str(json.dumps(response_json)))

    data_type = response_json["types"]
    types_list = []

    for type_info in data_type:
        types_list.append(type_info["type"]["name"])

    types = ", ".join(types_list)

    return PokemonSchema(name=response_json["name"], types=types)


print(pegar_pokemom(25))
