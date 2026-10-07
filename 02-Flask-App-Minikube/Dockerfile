FROM python:3.8-slim
WORKDIR /app
COPY . /app
RUN pip install --no-cache-dir --default-timeout=100 flask
CMD ["python", "app.py"]
