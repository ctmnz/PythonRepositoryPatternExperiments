from dataclasses import dataclass
from sqlalchemy.orm import registry, sessionmaker

import repository

from sqlalchemy import  create_engine
from sqlalchemy.orm import registry, sessionmaker

import orm
import model

mapping_registry = registry()

engine = create_engine('sqlite:///todo.sqlite')
mapping_registry.map_imperatively(model.Todo, orm.todo_tasks)
orm.metadata.create_all(bind=engine)
SessionLocal = sessionmaker(bind=engine)
session = SessionLocal()
repo = repository.SqlAlchemyRepository(session)

