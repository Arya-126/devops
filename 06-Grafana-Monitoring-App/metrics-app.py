from flask import Flask, Response, jsonify, request
from prometheus_client import Counter, Histogram, generate_latest, CONTENT_TYPE_LATEST
import time
import random

app = Flask(__name__)

REQUEST_COUNT = Counter('zepto_http_requests_total', 'Total HTTP Requests', ['method', 'endpoint', 'status'])
REQUEST_LATENCY = Histogram('zepto_http_request_duration_seconds', 'HTTP Request Latency', ['endpoint'])

@app.route('/')
def home():
    start_time = time.time()
    REQUEST_COUNT.labels(method=request.method, endpoint='/', status='200').inc()
    time.sleep(random.uniform(0.01, 0.05))
    REQUEST_LATENCY.labels(endpoint='/').observe(time.time() - start_time)
    return "Zepto Quick Commerce Operations Active\n"

@app.route('/order', methods=['POST', 'GET'])
def order():
    start_time = time.time()
    status = '200' if random.random() > 0.1 else '500'
    REQUEST_COUNT.labels(method=request.method, endpoint='/order', status=status).inc()
    time.sleep(random.uniform(0.02, 0.1))
    REQUEST_LATENCY.labels(endpoint='/order').observe(time.time() - start_time)
    return jsonify({"order_id": random.randint(1000, 9999), "status": "Placed" if status == '200' else "Failed"})

@app.route('/metrics')
def metrics():
    return Response(generate_latest(), mimetype=CONTENT_TYPE_LATEST)

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8000)
