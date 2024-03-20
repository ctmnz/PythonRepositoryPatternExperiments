from sqlalchemy import Table, Column, Integer, String, ForeignKey, create_engine, MetaData
from sqlalchemy.orm import registry, sessionmaker
from dataclasses import dataclass, field
from typing import Optional
import uuid
import abc


### Create data classes for User and Task

@dataclass
class User:
    id: int = field(init=False)
    name: str
    fullname: str
    nickname: str
    uuid: Optional[str] = field(default_factory=lambda: str(uuid.uuid4()))

@dataclass
class Task:
    id: int = field(init=False)
    title: str
    description: str
    uuid: Optional[str] = field(default_factory=lambda: str(uuid.uuid4()))


### Abstract Repository

class AbstractRepository(abc.ABC):
   @abc.abstractmethod
   def add(self, user: User):
       raise NotImplementedError

   def get(self, reference) -> User:
       raise NotImplementedError


## Concrete Repository
class SqlAlchemyRepository(AbstractRepository):
    def __init__(self, session):
        self.session = session

    def add(self, user: User):
        self.session.add(user)

    def get(self, reference) -> User:
        return self.session.query(User).filter_by(uuid=reference).one()

    def list(self):
        return self.session.query(User).all()

    def clean_up(self):
        self.session.query(User).delete()

## Small test

mapper_registry = registry()

## Table definition

user_table = Table(
        "users",
        mapper_registry.metadata,
        Column("id", Integer, primary_key=True),
        Column("uuid", String(40)),
        Column("name", String(50)),
        Column("fullname", String(50)),
        Column("nickname", String(12)),
)

task_table = Table(
        "tasks",
        mapper_registry.metadata,
        Column("id", Integer, primary_key=True),
        Column("uuid", String(40)),
        Column("title", String(50)),
        Column("description", String(255)),
)

## Create db connection
engine = create_engine("sqlite:///users.sqlite")

## Map the object User to the Database Table
mapper_registry.map_imperatively(User, user_table)
mapper_registry.map_imperatively(Task, task_table)
mapper_registry.metadata.create_all(bind=engine)

## Create session
Session = sessionmaker(bind=engine)
session = Session()

## Create reposiotry
repo = SqlAlchemyRepository(session)

## Create users and save them into the repository
u1 = User("Daniel", "Daniel Stoinov", "stnv")
u2 = User("John", "John Atanasov", "jjj")

print(repo.list())
repo.add(u1)
repo.add(u2)
print(repo.list())
print(repo.get(u1.uuid))
print(repo.get(u2.uuid))
print(repo.list())
repo.clean_up()
session.commit()
print(repo.list())
