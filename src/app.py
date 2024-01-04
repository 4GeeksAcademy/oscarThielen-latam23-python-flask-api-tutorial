from flask import Flask, jsonify, request

app = Flask(__name__)

todos = [
   { "label": "My first task", "done": False },
   { "label": "My second task", "done": False }
]

@app.route('/todos', methods=['GET','POST'])
def hello_world():
    if request.method == 'POST':
        response = add_new_todo()
        return response
    return jsonify(todos), 201
    

def add_new_todo():
    if request.method == 'POST':    
        request_body = request.get_json(force=True)
        print("Incoming request with the following body:", request_body)
        todos.append(request_body)
        return jsonify(todos)

@app.route('/todos/<int:position>', methods=['DELETE'])
def delete_todo(position):
    print("This is the position to delete: ", position)
    if position >= 0 and position < len(todos):
        deleted_todo = todos.pop(position)
        return jsonify(todos)
    else:
        return jsonify({"error": "Invalid position"}), 400

# These two lines should always be at the end of your app.py file.
if __name__ == '__main__':
    app.run(host='0.0.0.0', port=3245, debug=True)