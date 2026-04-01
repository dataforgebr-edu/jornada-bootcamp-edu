from pydantic import BaseModel


class PokemomSchema(BaseModel):
    name: str
    type: str
    height: int
    weight: int
