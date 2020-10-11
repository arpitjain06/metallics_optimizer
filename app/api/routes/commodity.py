from fastapi import APIRouter, Depends, HTTPException
from typing import List
from app.api.models.schema.commodity import Commodity, CommodityUp, CommodityFinal
from app.api.repository import db_manager

commodity = APIRouter()



# fake_movie_db = [
#     {
#         'name': 'Star Wars: Episode IX - The Rise of Skywalker',
#         'plot': 'The surviving members of the resistance face the First Order once again.',
#         'genres': ['Action', 'Adventure', 'Fantasy'],
#         'casts': ['Daisy Ridley', 'Adam Driver']
#     }
# ]


# @commodity.get('/fake/')
# async def index():
#     return fake_movie_db


@commodity.get('/commodity', response_model=List[Commodity])
async def get_commodity():
    return await db_manager.get_all_commodity()


# @commodity.get('/commodity/{id}', response_model=Commodity)
# async def get_commodity_by_id(id: int):
#     return await db_manager.get_commodity_by_id(id)


@commodity.get('/commodity/{id}')
async def get_commodity_final_by_id(id: int):
    comodity_details = await db_manager.get_commodity_by_id(id)
    qwerty = await db_manager.get_chemical_composition_comodity_by_id(id)
    chemical_composition = [
        {"element": {"id": row['id'], "name": row['name'],}, "percentage": row['percentage']} for row in qwerty]
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

# @commodity.get('/commodity_final/{id}')
# async def get_commodity_final_by_id(id: int):
#     comodity_details = await db_manager.get_commodity_by_id(id)
#     data =Commodity(**comodity_details)
#     print (data)
    
#     qwerty = await db_manager.get_chemical_composition_comodity_by_id(id)
#     for row in qwerty:
#         print(row['id'])
#     # return await db_manager.get_commodity_by_id(id)
#     return CommodityFinal(**comodity_details,
#     chemical_composition=qwerty)
