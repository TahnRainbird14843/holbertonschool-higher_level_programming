from flask import Flask, jsonify, abort, request
import json

app = Flask(__name__)

users = {}


@app.route("/")
def home():
    return "Welcome to the Flask API!"


@app.route("/data")
def data():
    return jsonify(list(users.keys()))


@app.route("/status")
def status():
    return "OK"


@app.route("/users/<username>")
def get_user(username):
    try:
        return jsonify(users[username])
    except:
        return jsonify({"error": "User not found"}), 404


@app.route("/add_user", methods=['POST'])
def add_user():
    if request.method == 'POST':
        try:
            data = request.get_json(force=True)
        except:
            return jsonify({"error": "Invalid JSON"}), 400
        if "username" not in list(data.keys()):
            return jsonify({"error": "Username is required"}), 400
        username = data["username"]
        if username in list(users.keys()):
            return jsonify({"error": "Username already exists"}), 409

        original_data = data
        del data["username"]
        users[username] = data
        message = {"message": "User added"}
        message["user"] = original_data
        return jsonify(message)



if __name__ == "__main__":
    app.run()