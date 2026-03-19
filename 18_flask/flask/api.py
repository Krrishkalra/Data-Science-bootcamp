### Put and Delete-- HTTP verbs
### Working with API's (json) and creating a flask API
### to create a "to do list application" ( add and remove tasks based on our requirement)

from flask import Flask, jsonify, request

app = Flask(__name__)

# intitial data for the to do list
tasks = [
    {
        'id':1,
        'name': "Item 1",
        'description': "This is item 1",
    },
    {
        'id':2,
        'name': "Item 2",
        'description': "This is item 2",
    }
]

@app.route('/')
def home():
    return "Welcome to the To Do List API"


# retrieve aall the the items in the to do list
@app.route('/tasks',methods=['GET'])
def get_tasks():
    return jsonify({'tasks': tasks})


# retrieve specific item based on the id
@app.route('/tasks/<int:task_id>', methods=['GET'])
def get_task(task_id):
    task = next((task for task in tasks if task['id']== task_id),None )
    if task is None:
        return jsonify({'message': 'Task not found'})
    return jsonify(task)

# add a new item to the to do list
@app.route('/tasks', methods = ['POST'])
def create_task():
    if not request.json or not 'name' in request.json :
        return jsonify({'message': 'task not found'})
    new_task = {
        'id': tasks[-1]["id"]+1 if tasks else 1,
        'name': request.json["name"],
        'description': request.json.get("description","")
        
    }
    tasks.append(new_task)
    return jsonify(new_task)


#PUT: update and existin task
@app.route('/tasks/<int:task_id>', methods = ['PUT'])
def update_task(task_id):
    task  = next((task for task in tasks if task['id']== task_id), None)
    if task is None:
        return jsonify({'message': 'Task not found'})
    task['name'] = request.json.get('name', task['name'])
    task['description'] = request.json.get('description', task['description'])
    return jsonify(task)


# DELETE-- delete and item
@app.route('/tasks/<int:task_id>', methods = ['DELETE'])
def delete_task(task_id):
    global tasks
    tasks = [task for task in tasks if task['id'] != task_id]
    return jsonify({'message': 'Task deleted successfully'})


if __name__ == "__main__":
    app.run(debug=True)