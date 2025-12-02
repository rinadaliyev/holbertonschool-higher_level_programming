from flask import Flask, jsonify, request

app = Flask(__name__)

# Store users in memory (start empty as required)
users = {}


# -------------------------------
#  Root endpoint
# -------------------------------
@app.route("/")
def home():
    return "Welcome to the Flask API!"


# -------------------------------
#  /status endpoint
# -------------------------------
@app.route("/status")
def status():
    return "OK"


# -------------------------------
#  /data endpoint
# Returns a list of all usernames
# -------------------------------
@app.route("/data")
def get_usernames():
    return jsonify(list(users.keys()))


# -------------------------------
#  /users/<username> endpoint
# Returns user object or 404
# -------------------------------
@app.route("/users/<username>")
def get_user(username):
    if username not in users:
        return jsonify({"error": "User not found"}), 404
    return jsonify(users[username])


# -------------------------------
#  /add_user (POST)
# Adds a new user to the dictionary
# -------------------------------
@app.route("/add_user", methods=["POST"])
def add_user():
    # Parse JSON safely
    try:
        data = request.get_json()
        if data is None:
            raise ValueError
    except Exception:
        return jsonify({"error": "Invalid JSON"}), 400

    # Validate username
    username = data.get("username")
    if not username:
        return jsonify({"error": "Username is required"}), 400

    # Check duplicate user
    if username in users:
        return jsonify({"error": "Username already exists"}), 409

    # Add the new user
    users[username] = {
        "username": username,
        "name": data.get("name"),
        "age": data.get("age"),
        "city": data.get("city")
    }

    return jsonify({
        "message": "User added",
        "user": users[username]
    }), 201


# -------------------------------
#  Run Flask dev server
# -------------------------------
if __name__ == "__main__":
    app.run()
