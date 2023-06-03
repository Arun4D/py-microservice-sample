import os
from sqlalchemy import (Column, Integer, Identity, MetaData, String, Table,
                        create_engine, ARRAY)

from databases import Database

if os.getenv('DATABASE_URL') is not None:
    DATABASE_URL = os.getenv('DATABASE_URL')
else:
    DATABASE_URL = 'postgresql://postgres:mysecretpassword@127.0.0.1:5432/postgres'

engine = create_engine(DATABASE_URL)
metadata = MetaData()

customers = Table(
    'customer',
    metadata,
    Column('id', Integer, Identity(always=True, start=1, cycle=True), primary_key=True),
    Column('firstName', String(250)),
    Column('lastName', String(250)),
    Column('dob', String(10)),
    Column('idNumber', String(250)),
    Column('idType', String(250))
)

database = Database(DATABASE_URL)