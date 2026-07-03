# ABC Technologies - Enterprise Cloud Website Deployment & DevOps Pipeline

**DevOps Assignment - 2 Submission**  
**Use Case Selected:** Use Case 1: Corporate Company Website Deployment (ABC Technologies)

---

## 📌 Project Overview
ABC Technologies is a next-generation corporate web application featuring responsive dark-mode UI, glassmorphic design elements, and interactive component architecture. This repository contains the complete source code alongside production-grade DevOps automation artifacts:
- **Source Code Management:** GitHub repository structure.
- **Continuous Integration / Continuous Deployment:** Declarative `Jenkinsfile` automating multi-stage validation, build, test, and rollout.
- **Containerization:** Ultra-slim production `Dockerfile` and Nginx server configuration (`nginx.conf`).
- **Kubernetes Orchestration:** Production manifests (`k8s/deployment.yaml` & `k8s/service.yaml`) featuring 3 replicas, readiness probes, and NodePort routing.
- **Observability Stack:** Docker Compose configuration running **Nagios**, **Graphite**, and **Grafana** (`monitoring/docker-compose.monitoring.yml`).

---

## 📂 Repository Structure
```
├── website/                  # Corporate Website Source Code
│   ├── index.html            # Home Page
│   ├── about.html            # About Us Page
│   ├── services.html         # Services Page
│   ├── careers.html          # Careers Page
│   ├── gallery.html          # Gallery Page
│   ├── contact.html          # Contact Us Page
│   ├── css/style.css         # Enterprise Design System
│   └── js/main.js            # Interactive JS Controller
├── nginx.conf                # Nginx Server Configuration & Health Checks
├── Dockerfile                # Multi-stage Container Specification
├── Jenkinsfile               # CI/CD Automation Pipeline
├── k8s/                      # Kubernetes Orchestration Manifests
│   ├── deployment.yaml       # K8s Deployment (3 Replicas + Health Probes)
│   └── service.yaml          # K8s NodePort Service (Port 30080)
└── monitoring/               # Telemetry & Availability Stack
    ├── docker-compose.monitoring.yml  # Graphite + Grafana + Nagios Suite
    └── generate_live_metrics.py       # Live Telemetry Streamer for Dashboards
```

---

## 🚀 Quick Start Guide

### Step 1: Run Website Locally via Docker
To verify the Docker container build and run the website locally:
```bash
# 1. Build the production Docker image
docker build -t abc-tech-website:latest .

# 2. Run container on localhost port 8081
docker run -d --name abc-website -p 8081:80 abc-tech-website:latest

# 3. Open in Browser
# Open http://localhost:8081 in your browser
```

---

### Step 2: Deploy to Kubernetes Cluster
If you are running Docker Desktop Kubernetes or Minikube:
```bash
# 1. Apply Deployment and Service manifests
kubectl apply -f k8s/deployment.yaml
kubectl apply -f k8s/service.yaml

# 2. Check running Pods
kubectl get pods -l app=abc-tech-website

# 3. Check Service Port
kubectl get svc abc-tech-website-service

# 4. Access deployed application
# For Docker Desktop K8s: Open http://localhost:30080
# For Minikube: Run `minikube service abc-tech-website-service`
```

---

### Step 3: Run Jenkins Automation Pipeline
1. Open Jenkins Dashboard (`http://localhost:8080`).
2. Create a new **Pipeline** job named `ABC-Tech-Website-Pipeline`.
3. Point the pipeline definition to **Pipeline script from SCM** (Git repository URL) or copy/paste the content of `Jenkinsfile`.
4. Click **Build Now** to watch stages execute: Checkout -> Validate -> Docker Build -> Container Test -> Kubernetes Rollout -> Verification.

---

### Step 4: Launch Monitoring Suite (Nagios, Graphite, Grafana)
We have provided an instant all-in-one monitoring suite via Docker Compose:
```bash
# 1. Start Graphite, Grafana, and Nagios containers
docker compose -f monitoring/docker-compose.monitoring.yml up -d

# 2. Start the live telemetry simulator in a terminal (pushes data to Graphite)
python3 monitoring/generate_live_metrics.py
```

**Access URLs & Credentials:**
- **Grafana Dashboard:** `http://localhost:3000` (Login: `admin` / `admin`)
  - *Data Source:* Configure Graphite at `http://devops-graphite:80`
- **Graphite Web UI:** `http://localhost:8085`
- **Nagios Monitoring:** `http://localhost:8083` (Login: `nagiosadmin` / `nagios`)

---

## 📸 Checklist for Assignment Documentation Screenshots
Make sure to capture these exact screenshots for your submission PDF report:
1. **GitHub Repository:** Screenshot showing code pushed to GitHub.
2. **Jenkins Dashboard & Build Console:** Screenshot of successful pipeline stages (all green) and console log showing `PIPELINE SUCCESS`.
3. **Docker Build & Container:** Terminal output showing `docker ps` with running container and browser view at `http://localhost:8081`.
4. **Kubernetes Deployment:** Output of `kubectl get pods` showing 3 pods `Running` and browser view at `http://localhost:30080`.
5. **Nagios Monitoring:** Screenshot of Nagios Host status (`UP`) and Service status (`OK`).
6. **Graphite Metrics:** Screenshot of Graphite dashboard receiving live CPU/Memory telemetry.
7. **Grafana Dashboards:** Screenshot of Grafana graphs visualizing CPU, Memory, Network, and Uptime.
