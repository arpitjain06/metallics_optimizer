from pydantic import BaseModel
from typing import List
# from app.api.models.domain.chemical import Chemical

class Composition(BaseModel):
    id: int
    chemical_id: int
    commodity_id: int
    percentage: int
