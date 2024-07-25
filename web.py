from flask import Flask, request, jsonify
from src.task_manager import TaskManager

app = Flask(__name__)
task_manager = TaskManager()

@app.route('/')
def home():
    return "Welcome to the To-Do List App"

@app.route('/tasks', methods=['GET', 'POST', 'DELETE'])
def tasks():
    if request.method == 'GET':
        tasks = task_manager.list_tasks()
        return jsonify(tasks)
    elif request.method == 'POST':
        description = request.json.get('description')
        due = request.json.get('due')
        task_manager.add_task(description, due)
        return jsonify({'status': 'Task added'})
    elif request.method == 'DELETE':
        index = request.json.get('index')
        task_manager.remove_task(index)
        return jsonify({'status': 'Task removed'})

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8000)
