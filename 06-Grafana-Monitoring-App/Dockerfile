FROM python:3.8-slim
WORKDIR /app
COPY . /app
RUN pip install --no-cache-dir flask prometheus_client
CMD ["python", "metrics-app.py"]
