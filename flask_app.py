from flask import Flask
import config


app = Flask(__name__)

@app.route("/")
def index_page():
    response = "<h1>TODOs</h1><ul>"
    tasks = config.repo.list()
    for task in tasks:
        response += f"<li>{task.title} - {task.uuid} </li>"
    response += "</ul>"
    return response

@app.route("/tasks/<uuid>")
def task_page(uuid):
    task = config.repo.get(uuid)
    response = f"<h1>Task</h1>Task Title:<b> {task.title}</b></br>Task Description: <b>{task.description}</b></br>"
    return response



if __name__=="__main__":
    app.run(debug=True)
