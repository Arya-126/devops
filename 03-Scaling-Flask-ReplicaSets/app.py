from flask import Flask, jsonify, request
import socket

app = Flask(__name__)

@app.route('/')
def home():
    return f"Zepto Flash Sale API - Served by Pod: {socket.gethostname()}\n"

@app.route('/buy', methods=['POST', 'GET'])
def buy():
    item = request.args.get('item', 'Quick Commerce Item')
    return jsonify({
        "status": "Order Placed Successfully",
        "item": item,
        "processed_by_pod": socket.gethostname()
    })

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=15000)
