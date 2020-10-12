from fastapi import APIRouter, Depends, HTTPException
from typing import List
from app.api.models.schema.commodity import Commodity, CommodityUp, CommodityFinal
from app.api.repository import db_manager

commodity = APIRouter()


@commodity.get('/commodity', response_model=List[Commodity])
async def get_commodity():
    return await db_manager.get_all_commodity()


@commodity.get('/commodity/{id}')
async def get_commodity_final_by_id(id: int):
    comodity_details = await db_manager.get_commodity_by_id(id)
    if not comodity_details:
        raise HTTPException(
            status_code=404,
            detail="commodity not found {}".format(id)
        )
    concentration = await db_manager.get_chemical_composition_comodity_by_id(id)
    total_percentage = sum([val['percentage'] for val in concentration])
    chemical_composition = [
        {
            "element": {
                "id": row['id'],
                "name": row['name']
            }, 
            "percentage": row['percentage']
        } for row in concentration]
    
    if total_percentage < 100:
        Unknown = {
            "element": {"id": 9999, "name": "Unknown"},
            "percentage": int(100-total_percentage)
        }
        chemical_composition.append(Unknown)
    return CommodityFinal(
            **comodity_details,
            chemical_composition=chemical_composition)


@commodity.put('/update_commodity/{id}', response_model=Commodity)
async def update_commodity(id: int, payload: CommodityUp):
    commodity = await db_manager.get_commodity_by_id(id)
    if not commodity:
        raise HTTPException(
            status_code=404,
            detail="commodity not found"
        )

    update_data = payload.dict(exclude_unset=True)
    commodity_in_db = CommodityUp(**commodity)
    commodity_updated = commodity_in_db.copy(update=update_data)
    return await db_manager.update_commodity(id, commodity_updated)


@commodity.post('/add_commodity', status_code=201)
async def post_commodity(payload: Commodity):
    commodity_id = await db_manager.add_commodity(payload)
    response = {
        'id': commodity_id,
        **payload.dict()
    }
    return response
