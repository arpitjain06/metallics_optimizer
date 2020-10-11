
from fastapi import APIRouter, Depends, HTTPException
from typing import List
from app.api.models.schema.composition import Composition
from app.api.repository import db_manager


composition = APIRouter()


@composition.get('/concentration', response_model=List[Composition])
async def get_composition():
    return await db_manager.get_all_composition()


@composition.post('/add_concentration', status_code=201)
async def post_composition(payload: Composition):
    composition_id = await db_manager.add_composition(payload)
    response = {
        'id': composition_id,
        **payload.dict()
    }
    return response


@composition.delete('/remove_chemical_composition/{chemical_composition_id}')
async def delete_composition(chemical_composition_id: int):
    chemical_composition = await db_manager.get_chemical_composition_by_id(
        chemical_composition_id
    )
    print(chemical_composition)
    if not chemical_composition:
        raise HTTPException(
            status_code=404,
            detail="chemical composition {} not found".format(chemical_composition_id)
        )
    return await db_manager.delete_chemical_composition(chemical_composition_id)


