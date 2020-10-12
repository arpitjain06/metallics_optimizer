from app.api.models.schema.chemical import Chemical
from app.api.models.schema.commodity import Commodity, CommodityUp
from app.api.models.schema.composition import Composition
from app.api.db import chemicals, database, commodity, chemical_composition


# chemical
async def add_chemical(payload: Chemical):
    query = chemicals.insert().values(**payload.dict())
    return await database.execute(query=query)


async def get_all_chemicals():
    query = chemicals.select()
    return await database.fetch_all(query=query)


# commodity
async def add_commodity(payload: Commodity):
    query = commodity.insert().values(**payload.dict())
    return await database.execute(query=query)


async def get_all_commodity():
    # query = commodity.select()
    # using SQl query
    query ="""
        select
            *
        from
            commodity
    """
    print(query)
    return await database.fetch_all(query=query)


async def get_commodity_by_id(id):
    query = commodity.select(commodity.c.id == id)
    return await database.fetch_one(query=query)


async def update_commodity(id: int, payload: CommodityUp):
    query = (
        commodity
        .update()
        .where(commodity.c.id == id)
        .values(**payload.dict())
    )
    return await database.execute(query=query)


async def get_all_composition():
    query = chemical_composition.select()
    return await database.fetch_all(query=query)


async def add_composition(payload: Composition):
    query = chemical_composition.insert().values(**payload.dict())
    return await database.execute(query=query)


async def get_chemical_composition_by_id(id):
    query = chemical_composition.select(chemical_composition.c.id == id)
    return await database.fetch_one(query=query)


async def delete_chemical_composition(id: int):
    query = chemical_composition.delete().where(chemical_composition.c.id == id)
    return await database.execute(query=query)


async def get_chemical_composition_comodity_by_id(id):
    query = """
        select
            cc.percentage as percentage,
            c.id as id,
            c.name as name
        from
            chemical_composition as cc
        join
            chemical as c 
        on
            cc.chemical_id = c.id
        where
            cc.commodity_id = {0};
    """.format(id)
    
    # query = chemical_composition.select(chemical_composition.c.commodity_id == id)
    return await database.fetch_all(query=query)
