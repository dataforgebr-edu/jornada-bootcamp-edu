import requests
from db import Base, SessionLocal, engine
from models import Pokemon
from schema import PokemomSchema

Base.metadata.create_all(bind=engine)


def fetch_pokemon_data(pokemon_id: int):
    response = requests.get(f"https://pokeapi.co/api/v2/pokemon/{pokemon_id}")
    if response.status_code == 200:
        data = response.json()
        types = ", ".join(tp["type"]["name"] for tp in data["types"])
        return PokemomSchema(
            name=data["name"], type=types, height=data["height"], weight=data["weight"]
        )
    else:
        return None


def add_pokemon_to_db(pokemon_schema: PokemomSchema) -> Pokemon:
    with SessionLocal() as db:
        db_pokemon = Pokemon(
            name=pokemon_schema.name,
            type=pokemon_schema.type,
            height=pokemon_schema.height,
            weight=pokemon_schema.weight,
        )
        db.add(db_pokemon)
        db.commit()
    return db_pokemon
