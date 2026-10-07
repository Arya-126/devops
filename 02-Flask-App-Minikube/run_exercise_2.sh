#!/bin/bash
cd /mnt/c/Users/arya1/OneDrive/Desktop/devops/02-Flask-App-Minikube
echo "=== Starting Minikube ==="
minikube start
echo "=== Building Docker Image ==="
docker build --network=host -t flask-app:latest .
echo "=== Loading Image to Minikube ==="
minikube image load flask-app:latest
echo "=== Applying Deployment ==="
kubectl apply -f flask-deployment.yaml
sleep 5
echo "=== Deployments ==="
kubectl get deployments
echo "=== Pods ==="
kubectl get pods -l app=flask-app
echo "=== Describe Deployment ==="
kubectl describe deployment flask-app
echo "=== Services ==="
kubectl get services
echo "=== Pod Logs ==="
POD_NAME=$(kubectl get pods -l app=flask-app -o jsonpath='{.items[0].metadata.name}')
echo "Pod Name: $POD_NAME"
kubectl logs $POD_NAME
echo "=== Testing App Response ==="
kubectl exec $POD_NAME -- curl -s http://localhost:15000
