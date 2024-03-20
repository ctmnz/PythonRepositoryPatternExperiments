from abc import ABC, abstractmethod
import unittest
import uuid
from sqlalchemy import Table, MetaData, Integer, Boolean, Column, String,  create_engine
from sqlalchemy.orm import registry, sessionmaker
from dataclasses import dataclass, field
from typing import Optional

class Task(ABC):
    pass

@dataclass
class TodoTask(Task):
    id: int = field(init=False)
    title: str
    description: str
    is_done: bool = False
    uuid: Optional[str] = field(default_factory=lambda: str(uuid.uuid4()))

## Create Abstract Repository
class AbstractRepository(ABC):
    @abstractmethod
    def add(self, Task):
        raise NotImplementedError

    @abstractmethod
    def get(self, reference) -> Task:
        raise NotImplementedError

## Create Concrete Repostitory
class TodoRepository(AbstractRepository):
    def __init__(self, session):
        self.session = session

    def add(self, task: TodoTask):
        self.session.add(task)
        self.session.commit()

    def get(self, uuid):
        return self.session.query(TodoTask).filter_by(uuid=uuid).one() 

    def list_tasks(self):
        return self.session.query(TodoTask).all()

    def clean_up(self):
        self.session.query(TodoTask).delete()
        self.session.commit()

    def update(self, task: TodoTask):
        self.session.query(TodoTask).update(task)
        self.session.commit()

    def delete(self, task: TodoTask):
        self.session.delete(task)
        self.session.commit()


    def __str__(self):
        tasks = self.session.query(TodoTask).all()
        output = ""
        for task in tasks:
            output +=f"[Done={task.is_done}] {task.title}: {task.description}\n"
        return output




## Todo class without repository. Old way of doing it
class TODO():
    def __init__(self):
        self.list_of_tasks = []

    def add_task(self, title: str, description: str):
        t = TodoTask(title=title, description=description, is_done=False)
        self.list_of_tasks.append(t)

    def delete_task(self, task_index: int):
        del self.list_of_tasks[task_index]

    def list_tasks(self):
        print("========================================================")
        for task in self.list_of_tasks:
            print(f"task: [{task.is_done}] {task.title}: {task.description}")

mapping_registry = registry()


todo_tasks = Table(
        'todo_tasks', mapping_registry.metadata,
        Column('id', Integer, primary_key=True, autoincrement=True),
        Column('uuid', String(50)),
        Column('title', String(255)),
        Column('description', String(255)),
        Column('is_done', Boolean),
)

engine = create_engine("sqlite:///todo.sqlite")
mapping_registry.map_imperatively(TodoTask, todo_tasks)
mapping_registry.metadata.create_all(bind=engine)

# Create an engine (replace with your connection string)

# Create a session class bound to the engine
SessionLocal = sessionmaker(bind=engine)

# Create a session
session = SessionLocal()

# Create the concrete Todo repo
todo_repo = TodoRepository(session)



class Test(unittest.TestCase):
    def test_initial(self):
        mytodo = TODO()
        mytodo.add_task("Create TODO aggregate", "You will need to create task aggregate!")
        mytodo.add_task("Create 2 TODO aggregate", "You will need to create task aggregate!")
        mytodo.list_tasks()
        mytodo.delete_task(1)
        mytodo.list_tasks()

    def test_repo(self):
        todo_repo = TodoRepository(session)
        task1 = TodoTask(title="Initial task", description="Do something initially")
        task2 = TodoTask(title="Generic Task 2", description="Do something: task 2")
        task3 = TodoTask(title="Better task", description="Create better task description")
        todo_repo.add(task1)
        todo_repo.add(task2)
        todo_repo.add(task3)
        print(todo_repo.list_tasks())
        print(todo_repo)
        todo_repo.delete(task1)
        print(todo_repo)
        task2.title = "Not so generic"
        session.commit()
        print(todo_repo)
        todo_repo.clean_up()

        


        
def main():
    unittest.main()

if __name__=="__main__":
    main()





