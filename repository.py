from abc import ABC, abstractmethod 
import model


class AbstractRepository(ABC):
    @abstractmethod
    def add(self, todo: model.Todo):
        raise NotImplementedError

    @abstractmethod
    def get(self, uuid: str):
        raise NotImplementedError

class SqlAlchemyRepository(AbstractRepository):
    def __init__(self, session):
        self.session = session

    def get(self, uuid: str):
        return self.session.query(model.Todo).filter_by(uuid=uuid).one()

    def add(self, todo: model.Todo):
        self.session.add(todo)

    def list(self):
        return self.session.query(model.Todo).all()
