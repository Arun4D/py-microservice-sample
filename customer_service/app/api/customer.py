from typing import List
from fastapi import Header, APIRouter, HTTPException

from app.api.models import Customer, CustomerIn, CustomerOut
from app.api import db_manager

customers = APIRouter()

@customers.get('/', response_model=List[CustomerOut])
async def index():
    customers =  await db_manager.get_all_customers()
    return customers

@customers.post('/', status_code=201, response_model=CustomerOut)
async def add_customer(payload: CustomerIn):
    customerInDb = Customer(**payload.dict())
    customer_id = await db_manager.add_customer(customerInDb)
    customer = customerInDb.dict()
    customer['id'] = customer_id
    response = CustomerOut(**customer)
    return response

@customers.put('/{id}', response_model=CustomerOut)
async def update_customer(id: int, payload: CustomerIn):
    customer = await db_manager.get_customer(id)
    if not customer:
        raise HTTPException(status_code=404, detail="Customer not found")

    update_data = payload.dict(exclude_unset=True)
    customer_db = Customer(**customer)

    updated_customer = customer_db.copy(update=update_data)
    updated_customer_l = updated_customer.dict() 
    del updated_customer_l['id'] 
    customer_id =  await db_manager.update_customer(id, updated_customer_l)
    response = CustomerOut(**payload.dict())

    return response

@customers.delete('/{id}')
async def delete_customer(id: int):
    customer = await db_manager.get_customer(id)
    if not customer:
        raise HTTPException(status_code=404, detail="Customer not found")
    customer_id =  await db_manager.delete_customer(id)
    response = {
        'message': 'Deleted'
    }

    return response