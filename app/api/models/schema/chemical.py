from pydantic import BaseModel
from typing import List


class Chemical(BaseModel):
    id: int
    name: str
