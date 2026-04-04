from typing import Union

from pydantic import BaseModel, PositiveFloat


class ItemBase(BaseModel):
    name: str
    price: PositiveFloat
    is_offer: Union[bool, None] = None


class ItemCreate(ItemBase):
    pass


class Item(ItemBase):
    id: int
