from typing import List
from fastapi import APIRouter, Depends, HTTPException
from fastapi import Header, APIRouter

from app.api.models.schema.chemical import Chemical
from app.api.repository import db_manager


chemical = APIRouter()


@chemical.get('/', response_model=List[Chemical])
async def get_chemical():
    return await db_manager.get_all_chemicals()


@chemical.post('/add_chemical', status_code=201)
async def post_chemical(payload: Chemical):
    chemical = await db_manager.add_chemical(payload)
    # if not chemical:
    #     raise HTTPException(
    #         status_code=404,
    #         detail="Duplicate id"
    #     )
    response = {
        'id': chemical,
        **payload.dict()
    }
    return response
