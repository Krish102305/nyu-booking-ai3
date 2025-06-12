{\rtf1\ansi\ansicpg1252\cocoartf2758
\cocoatextscaling0\cocoaplatform0{\fonttbl\f0\fswiss\fcharset0 Helvetica;}
{\colortbl;\red255\green255\blue255;}
{\*\expandedcolortbl;;}
\margl1440\margr1440\vieww29200\viewh18400\viewkind0
\pard\tx1440\tx2160\tx2164\tx2880\tx3600\tx4320\tx5040\tx5760\tx6480\tx7200\tx7920\tx8640\pardirnatural\partightenfactor0

\f0\fs24 \cf0 from flask import Flask, request, jsonify\
from book_room import book_bobst_room\
\
app = Flask(__name__)\
\
@app.route('/book-room', methods=['POST'])\
def handle_booking():\
    data = request.json\
    username = data.get("username")\
    password = data.get("password")\
    booking_time = data.get("time")\
\
    result = book_bobst_room(username, password, booking_time)\
    return jsonify(result)\
\
if __name__ == '__main__':\
    app.run(port=5000, debug=True)\
}