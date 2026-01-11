from flask import Flask, request, jsonify

app = Flask(__name__)
bookings = {}

@app.route('/bookings', methods=['POST'])
def create_booking():
    data = request.json
    bookings[data['id']] = data
    return jsonify({"message": "Booking created"}), 201

@app.route('/bookings', methods=['GET'])
def list_bookings():
    return jsonify(bookings)

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5002)
