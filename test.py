import unittest
from sqlalchemy.sql import text
import model
import config


# Tests
class TestTodo(unittest.TestCase):
    def test_todo_creation(self):
        todo1 = model.Todo(title="First Task", description="Create a todo application")
        self.assertEqual(todo1.title, "First Task")
        self.assertEqual(todo1.description, "Create a todo application")

    def test_todo_marking_done_undone(self):
        todo1 = model.Todo(title="First Task", description="Create a todo application")
        todo1.mark_as_done()
        self.assertEqual(todo1.is_done, True)
        todo1.mark_as_undone()
        self.assertEqual(todo1.is_done, False)

    def test_repository_can_save_todo(self):
        ## Cleanup the database
        config.session.query(model.Todo).delete()
        config.session.commit()
     
        todo1 = model.Todo(title="First Task", description="Create a todo application")
        config.repo.add(todo1)
        config.session.commit()
        rows = config.session.execute(text('SELECT title, description, is_done FROM "todo_tasks"'))
        assert list(rows) == [("First Task", "Create a todo application", False)]
        
        ## Cleanup the database
        config.session.query(model.Todo).delete()
        config.session.commit()


    def test_repository_can_save_the_status(self):
        ## Cleanup the database
        config.session.query(model.Todo).delete()
        config.session.commit()
        
        todo1 = model.Todo(title="To be done", description="Task that should be done")
        config.repo.add(todo1)
        config.session.commit()
        rows = config.session.execute(text('SELECT title, description, is_done FROM "todo_tasks"'))
        assert list(rows) == [("To be done", "Task that should be done", False)]
        todo1.mark_as_done()
        config.session.commit()
        rows = config.session.execute(text('SELECT title, description, is_done FROM "todo_tasks"'))
        assert list(rows) == [("To be done", "Task that should be done", True)]
        todo1.mark_as_undone()
        config.session.commit()
        rows = config.session.execute(text('SELECT title, description, is_done FROM "todo_tasks"'))
        assert list(rows) == [("To be done", "Task that should be done", False)]
        
        ## Cleanup the database
        config.session.query(model.Todo).delete()
        config.session.commit()

# Main part Start the tests 

def main():
    unittest.main()

if __name__=="__main__":
    main()
