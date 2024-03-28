from dataclasses import dataclass, field
from typing import Optional
import uuid

# Model
@dataclass
class Todo():
    title: str
    description: str
    is_done: bool = False
    id: int = field(init=False)
    uuid: Optional[str]=field(default_factory=lambda : str(uuid.uuid4()))

    def mark_as_done(self):
        self.is_done = True

    def mark_as_undone(self):
        self.is_done = False

