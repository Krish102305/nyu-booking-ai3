from flask import Flask, request, jsonify
from book_room import book_bobst_room

app = Flask(__name__)

@app.route('/book-room', methods=['POST'])
def handle_booking():
    data = request.json
    username = data.get("username")
    password = data.get("password")
    time = data.get("time")

    if not username or not password or not time:
        return jsonify({"error": "Missing required field(s)"}), 400

    result = book_bobst_room(username, password, time)
    return jsonify(result)

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)