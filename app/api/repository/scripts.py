from app.api.db import database

async def migrations():
    tables = ["chemical", "commodity", "chemical_composition"]
    for table in tables:
        query = "DELETE FROM {0}".format(table)
        await database.execute(query=query)

    chemical = """
        INSERT INTO chemical (id, name) VALUES 
            (0, 'C'),
            (1, 'N'),
            (2, 'O'),
            (3, 'Ai');
    """
    await database.execute(query=chemical)
    comodity = """
        INSERT INTO commodity (id, name, inventory, price) VALUES 
            (0, 'Plate & Structural', 124.50, 800),
            (1, 'Plate', 224.50, 700),
            (2, 'Structural', 34.50, 500),
            (3, 'Comodities Structural', 554.50, 1000),
            (4, 'Como_Structural', 60.50, 50);
    """
    await database.execute(query=comodity)

    chemical_composition = """
        INSERT INTO chemical_composition (id, chemical_id, commodity_id, percentage) VALUES 
            (0, 0, 0, 50),
            (1, 1, 0, 20),
            (2, 2, 0, 30),
            (3, 0, 1, 60),
            (4, 1, 1, 20),
            (5, 2, 1, 20),
            (6, 0, 2, 35),
            (7, 1, 2, 30),
            (8, 2, 2, 10),
            (9, 3, 2, 25),
            (10, 0, 3, 35),
            (11, 1, 3, 30),
            (12, 2, 3, 10);
            
    """
    await database.execute(query=chemical_composition)