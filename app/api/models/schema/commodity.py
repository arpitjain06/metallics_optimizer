from pydantic import BaseModel
from typing import List



class Percentage(BaseModel):
    element: dict
    percentage: int

class CommodityFinal(BaseModel):
    id: int
    name: str
    price: float
    inventory: float
    chemical_composition: List[Percentage]


class Commodity(BaseModel):
    id: int
    name: str
    price: float
    inventory: float


class CommodityUp(BaseModel):
    name: str
    price: float


