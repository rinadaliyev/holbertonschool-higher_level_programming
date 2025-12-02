from flask import Flask, jsonify, request
from flask_httpauth import HTTPBasicAuth
from flask_jwt_extended import (
    JWTManager, create_access_token, jwt_required,
    get_jwt_identity
)
from werkzeug.security import generate_password_hash, check_password_hash

app = Flask(__name__)

# Secret key for JWT
app.config["JWT_SECRET_KEY"] = "super-secret-key-change-this"

# Setup Basic Auth and JWT
auth = HTTPBasicAuth()
jwt = JWTManager(app)

# -----------------------------
# In-memory user store
# -----------------------------
users = {
    "user1": {
        "username": "user1",
        "password": generate_password_hash("password"),
        "role": "user"
    },
    "admin1": {
        "username": "admin1",
        "password": generate_password_hash("password"),
        "role": "admin"
    }
}

# -----------------------------
# BASIC AUTHENTICATION
# -----------------------------
@auth.verify_password
def verify_password(username, password):
    if username in users and check_password_hash(users[username]["password"], password):
        return username
    return None

@auth.error_handler
def unauthorized():
    return jsonify({"error": "Unauthorized"}), 401


@app.route("/basic-protected")
@auth.login_required
def basic_protected():
    return "Basic Auth: Access Granted"


# -----------------------------
# JWT AUTHENTICATION
# -----------------------------
@app.route("/login", methods=["POST"])
def login():
    data = request.get_json()

    if not data or "username" not in data or "password" not in data:
        return jsonify({"error": "Invalid credentials"}), 401

    username = data["username"]
    password = data["password"]

    if username not in users or not check_password_hash(users[username]["password"], password):
        return jsonify({"error": "Invalid credentials"}), 401

    # Create JWT token containing username + role
    access_token = create_access_token(
        identity={
            "username": username,
            "role": users[username]["role"]
        }
    )

    return jsonify({"access_token": access_token})


@app.route("/jwt-protected")
@jwt_required()
def jwt_protected():
    return "JWT Auth: Access Granted"


# -----------------------------
# ROLE-BASED ACCESS
# -----------------------------
@app.route("/admin-only")
@jwt_required()
def admin_only():
    identity = get_jwt_identity()

    if identity["role"] != "admin":
        return jsonify({"error": "Admin access required"}), 403

    return "Admin Access: Granted"


# -----------------------------
# JWT ERROR HANDLERS (must return 401)
# -----------------------------
@jwt.unauthorized_loader
def handle_unauthorized_error(err):
    return jsonify({"error": "Missing or invalid token"}), 401

@jwt.invalid_token_loader
def handle_invalid_token_error(err):
    return jsonify({"error": "Invalid token"}), 401

@jwt.expired_token_loader
def handle_expired_token_error(jwt_header, jwt_data):
    return jsonify({"error": "Token has expired"}), 401

@jwt.revoked_token_loader
def handle_revoked_token_error(jwt_header, jwt_data):
    return jsonify({"error": "Token has been revoked"}), 401

@jwt.needs_fresh_token_loader
def handle_needs_fresh_token_error(jwt_header, jwt_data):
    return jsonify({"error": "Fresh token required"}), 401


# -----------------------------
# Run server
# -----------------------------
if __name__ == "__main__":
    app.run()
