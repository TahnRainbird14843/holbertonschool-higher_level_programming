from flask import Flask, jsonify, abort, request
import json

app = Flask(__name__)

users = {}


@app.route("/")
def home():
    return "Welcome to the Flask API"


@app.route("/data")
def data():
    return jsonify(list(users.keys()))


@app.route("/status")
def status():
    return "OK"


@app.route("/users/<username>")
def get_user(username):
    try:
        return users[username]
    except:
        abort(404, {"error": "User not found"})


@app.route("/add_user", methods=['POST'])
def add_user():
    if request.method == 'POST':
        data = request.form
        try:
            data = json.loads(data)
        except:
            abort(400, {"error": "Invalid JSON"})
        if "username" not in list(data.keys()):
            abort(400, {"error": "Username is required"})
        username = data["username"]
        if username in list(users.values()):
            abort(409, {"error": "Username already exists"})

        original_data = data
        del data["username"]
        users[username] = data
        message = {"message": "User added"}
        message["user"] = original_data
        return jsonify(message)



if __name__ == "__main__":
    app.run()