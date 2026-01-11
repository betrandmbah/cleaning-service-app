from flask import Flask, request, jsonify

app = Flask(__name__)

users = {}

@app.route('/users', methods=['POST'])
def create_user():
    data = request.json
    users[data['id']] = data
    return jsonify({"message": "User created"}), 201

@app.route('/users/<user_id>', methods=['GET'])
def get_user(user_id):
    return jsonify(users.get(user_id, {}))

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5001)
