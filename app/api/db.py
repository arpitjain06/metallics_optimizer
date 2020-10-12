from sqlalchemy import (Column, Integer, MetaData, String, Table, ForeignKey,
                        create_engine, Float)

from databases import Database

DATABASE_URL = 'postgresql://postgres:newPassword@localhost/test'

engine = create_engine(DATABASE_URL)
metadata = MetaData()

chemicals = Table(
    'chemical',
    metadata,
    Column('id', Integer, primary_key=True),
    Column('name', String(50)),
)

commodity = Table(
    'commodity',
    metadata,
    Column('id', Integer, primary_key=True),
    Column('name', String(50)),
    Column('inventory', Float),
    Column('price', Float),
)

chemical_composition = Table(
    'chemical_composition',
    metadata,
    Column('id', Integer, primary_key=True),
    Column('chemical_id', Integer, ForeignKey("chemical.id", ondelete='CASCADE')),
    Column('commodity_id', Integer, ForeignKey("commodity.id", ondelete='CASCADE')),
    Column('percentage', Integer)
)


database = Database(DATABASE_URL)
