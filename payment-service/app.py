from flask import Flask, request, jsonify

app = Flask(__name__)
payments = {}

@app.route('/payments', methods=['POST'])
def process_payment():
    data = request.json
    payments[data['id']] = data
    return jsonify({"message": "Payment processed"}), 201

@app.route('/payments', methods=['GET'])
def list_payments():
    return jsonify(payments)

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5004)
