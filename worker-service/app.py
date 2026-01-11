from flask import Flask, request, jsonify

app = Flask(__name__)
workers = {}

@app.route('/workers', methods=['POST'])
def add_worker():
    data = request.json
    workers[data['id']] = data
    return jsonify({"message": "Worker added"}), 201

@app.route('/workers', methods=['GET'])
def list_workers():
    return jsonify(workers)

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5003)
