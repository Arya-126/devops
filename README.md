# DevOps & Kubernetes Hands-on Exercises Repository

Welcome to the **DevOps & Kubernetes Hands-on Laboratory Solutions Repository**. This repository contains detailed, production-grade solutions for Exercises 01 through 10 from [SunagP/DevOps-Lab](https://github.com/SunagP/DevOps-Lab) alongside an automated **GitHub Actions** deployed **Developer & DevOps Engineering Portfolio**.

Each exercise folder contains full source code, Kubernetes manifest files, deployment scripts, visual architecture walkthroughs, verification tables, and dark-theme screenshots demonstrating step-by-step execution.

---

## 🚀 GitHub Actions Continuous Deployment Workflow

This repository includes an automated GitHub Actions deployment pipeline located at [`.github/workflows/deploy.yml`](./.github/workflows/deploy.yml).

When code is pushed to the `main` branch, the workflow automatically builds and deploys the static portfolio site to **GitHub Pages**.

---

## 📚 Master Exercises & Portfolio Index

| # | Folder Name | Primary Technologies | Key Concepts Covered | Status | README Link |
| :---: | :--- | :--- | :--- | :---: | :---: |
| **00** | **00-Portfolio** | HTML5, CSS3, JS, GitHub Actions | Software Engineer & DevOps Portfolio, GitHub Pages CI/CD | ✅ Deployed | [View README](./00-Portfolio/README.md) |
| **01** | **01-Nginx-Pod** | Kubernetes, YAML, Nginx | Pod spec, NodePort Service, kubectl commands | ✅ Completed | [View README](./01-Nginx-Pod/README.md) |
| **02** | **02-Flask-App-Minikube** | Minikube, Docker, Flask, K8s | Containerizing Flask, Deployment manifests, Minikube Tunnel | ✅ Completed | [View README](./02-Flask-App-Minikube/README.md) |
| **03** | **03-Scaling-Flask-ReplicaSets** | Kubernetes, ReplicaSets, Flask | High availability, Pod scaling (`kubectl scale`), Self-healing | ✅ Completed | [View README](./03-Scaling-Flask-ReplicaSets/README.md) |
| **04** | **04-Docker-Networking** | Docker, Docker Compose, Flask | Custom bridge networks, Container DNS, Inter-container connectivity | ✅ Completed | [View README](./04-Docker-Networking/README.md) |
| **05** | **05-Docker-Security-AppArmor** | AppArmor, Docker, SecurityContext | Linux security profiles, Restricting sys-calls, Pod SecurityContext | ✅ Completed | [View README](./05-Docker-Security-AppArmor/README.md) |
| **06** | **06-Grafana-Monitoring-App** | Prometheus, Grafana, Flask, K8s | Prometheus metrics exporter, Grafana dashboards, Pod monitoring | ✅ Completed | [View README](./06-Grafana-Monitoring-App/README.md) |
| **07** | **07-Jenkins-CI-Automation** | Jenkins, Docker, CI/CD | Jenkins installation, Containerized Jenkins setup, Admin credentials | ✅ Completed | [View README](./07-Jenkins-CI-Automation/README.md) |
| **08** | **08-Jenkins-Hello-World-Job** | Jenkins, Shell Scripting, Git | Freestyle jobs, SCM triggers, Automated build steps | ✅ Completed | [View README](./08-Jenkins-Hello-World-Job/README.md) |
| **09** | **09-Jenkins-Multi-Stage-Pipeline** | Jenkinsfile, Python, Unit Testing | Multi-stage declarative pipelines (Build, Test, Deploy), Stage View | ✅ Completed | [View README](./09-Jenkins-Multi-Stage-Pipeline/README.md) |
| **10** | **10-Multi-Node-Multi-App-Deployment** | Minikube Multi-Node, PodAntiAffinity | 3-Node Minikube cluster, Pod Anti-Affinity rules, E-commerce microservices | ✅ Completed | [View README](./10-Multi-Node-Multi-App-Deployment/README.md) |

---

## 🛠️ Repository Standards & Layout
Every exercise follows a standardized structure based on production DevOps guidelines:
* **Code & Manifest Files:** Native YAML manifests (`.yaml`), Dockerfiles (`Dockerfile`), Python apps (`.py`), and Shell scripts (`.sh`).
* **Visual Screenshots (`screenshot/`):** Pixel-perfect PNG captures of terminal commands, Minikube services, and web dashboards.
* **Detailed `README.md`:** Comprehensive execution guides, architecture diagrams, verification tables, and troubleshooting FAQs.

---

## 🚀 Quick Start
To run any exercise locally:
```bash
# Example: Navigating to Exercise 10
cd 10-Multi-Node-Multi-App-Deployment

# View deployment commands and manifests
cat README.md
```
