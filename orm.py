from sqlalchemy import MetaData, Table, Column, Integer, String, Boolean, create_engine
from sqlalchemy.orm import registry, sessionmaker
from sqlalchemy.sql import text

import model
import repository

# ORM stuff
metadata = MetaData()

todo_tasks = Table(
        'todo_tasks', metadata,
        Column('id', Integer, primary_key=True, autoincrement=True),
        Column('title', String(50)),
        Column('description', String(255)),
        Column('uuid', String(50)),
        Column('is_done', Boolean),
)


