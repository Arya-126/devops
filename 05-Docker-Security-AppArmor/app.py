from flask import Flask, jsonify
import os

app = Flask(__name__)

@app.route('/')
def index():
    return "AppArmor Secured Flask Service Running!\n"

@app.route('/read-etc')
def read_etc():
    try:
        files = os.listdir('/etc')
        return jsonify({"status": "Allowed", "count": len(files)})
    except Exception as e:
        return jsonify({"status": "Blocked by AppArmor Profile", "error": str(e)}), 403

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
