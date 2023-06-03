from pydantic import BaseModel
from typing import List, Optional

class CustomerIn(BaseModel):
    id: int
    firstName: str
    lastName: str
    dob: str
    idNumber: str
    idType: str

class Customer(BaseModel):
    id: int
    firstName: str
    lastName: str
    dob: str
    idNumber: str
    idType: str

class CustomerOut(BaseModel):
    id: int
    firstName: str
    lastName: str
    dob: str
    idNumber: str
    idType: str