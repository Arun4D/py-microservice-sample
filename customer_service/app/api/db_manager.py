from app.api.models import Customer, CustomerIn, CustomerOut
from app.api.db import customers, database


async def add_customer(payload: Customer):
    customer = payload.dict()
    del customer['id'] 
    query = customers.insert().values(customer)

    return await database.execute(query=query)

async def get_all_customers():
    query = customers.select()
    return await database.fetch_all(query=query)

async def get_customer(id):
    query = customers.select(customers.c.id==id)
    return await database.fetch_one(query=query)

async def delete_customer(id: int):
    query = customers.delete().where(customers.c.id==id)
    return await database.execute(query=query)

async def update_customer(id: int, payload: Customer):
    query = (
        customers
        .update()
        .where(customers.c.id == id)
        .values(**payload)
    )
    return await database.execute(query=query)
