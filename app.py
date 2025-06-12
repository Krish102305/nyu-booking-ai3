from flask import Flask, request, jsonify
from book_room import book_bobst_room

app = Flask(__name__)

@app.route('/book-room', methods=['POST'])
def handle_booking():
    data = request.json
    username = data.get("username")
    password = data.get("password")
    booking_time = data.get("time")

    result = book_bobst_room(username, password, booking_time)
    return jsonify(result)

if __name__ == '__main__':
    app.run(port=5000, debug=True)
