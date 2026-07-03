# Complete Step-by-Step Guide: How to Configure, Visualize & Capture Screenshots

Since you already have **Docker**, **Kubernetes**, **Jenkins**, and **GitHub** installed on your Mac, follow this exact step-by-step procedure to execute the project, visualize every stage, and capture the exact screenshots required for your **Assignment - 2 PDF Report**.

---

## 🛠️ Step 1: Push Code to GitHub Repository
1. Open your terminal in this project directory:
   ```bash
   cd /Users/baijuyadav/Desktop/23BBS0179_Baiju_Yadav_DevOps_Project
   ```
2. Initialize Git and push to your GitHub repo:
   ```bash
   git init
   git add .
   git commit -m "Initial commit: ABC Technologies DevOps Enterprise Project"
   git branch -M main
   # Replace <YOUR_GITHUB_REPO_URL> with your actual repository URL
   git remote add origin <YOUR_GITHUB_REPO_URL>
   git push -u origin main
   ```
3. **📸 Screenshot #1 (GitHub Repository):**
   - Open your GitHub repository URL in your web browser.
   - Take a clear screenshot showing all folders (`website/`, `k8s/`, `monitoring/`, `Dockerfile`, `Jenkinsfile`).

---

## 🛠️ Step 2: Test & Visualize Docker Containerization
1. Build and run the Docker container locally:
   ```bash
   docker build -t abc-tech-website:latest .
   docker run -d --name abc-website -p 8081:80 abc-tech-website:latest
   docker ps
   ```
2. **📸 Screenshot #2 (Docker Build & Running Container):**
   - Take a screenshot of your terminal showing `docker ps` with `abc-website` status `Up`.
   - Open your browser to `http://localhost:8081`. Take a screenshot of the **stunning dark-mode Home Page** of ABC Technologies running locally.

---

## 🛠️ Step 3: Test & Visualize Kubernetes Deployment
1. Ensure your local Kubernetes cluster is active (e.g., enable Kubernetes in Docker Desktop settings or start Minikube).
2. Apply the Kubernetes deployment and service manifests:
   ```bash
   kubectl apply -f k8s/deployment.yaml
   kubectl apply -f k8s/service.yaml
   kubectl get pods
   kubectl get svc abc-tech-website-service
   ```
3. **📸 Screenshot #3 (Kubernetes Deployment):**
   - Take a terminal screenshot showing `kubectl get pods` with 3 replicas of `abc-tech-website-deployment` in the `Running` state (`1/1`).
   - Open your browser to `http://localhost:30080` (or the Minikube IP/port). Take a browser screenshot verifying the website is served from Kubernetes!

---

## 🛠️ Step 4: Configure Jenkins CI/CD Automation
1. Start your local Jenkins server and open `http://localhost:8080` in your browser.
2. Click **New Item** -> Name it `ABC-Tech-Website-Pipeline` -> Select **Pipeline** -> Click **OK**.
3. Under the **Pipeline** section:
   - **Definition:** Select `Pipeline script from SCM`.
   - **SCM:** Select `Git`.
   - **Repository URL:** Paste your GitHub repository URL.
   - **Script Path:** `Jenkinsfile`.
4. Click **Save** and then click **Build Now**.
5. **📸 Screenshot #4 (Jenkins Automation & Build URL):**
   - Take a screenshot of the **Jenkins Stage View** showing all 6 stages completed in green (`Checkout Code`, `Validate Source Code`, `Build Docker Image`, `Test Docker Container`, `Deploy to Kubernetes`, `Verify K8s Deployment`).
   - Click on the build number (`#1`) -> Click **Console Output**. Scroll to the bottom showing `🎉 PIPELINE SUCCESS` and take a screenshot.

---

## 🛠️ Step 5: Configure & Visualize Monitoring Stack (Nagios, Graphite, Grafana)
We have made configuring monitoring **effortless** by packaging Nagios, Graphite, and Grafana into Docker Compose.

1. Launch the monitoring suite:
   ```bash
   docker compose -f monitoring/docker-compose.monitoring.yml up -d
   docker ps | grep devops-
   ```
2. Start the live telemetry generator script in a terminal window (keep it running while taking screenshots):
   ```bash
   python3 monitoring/generate_live_metrics.py
   ```
   *(You will see log lines showing live metrics being transmitted every 3 seconds).*

---

### 📊 Visualizing Graphite Metrics
1. Open your browser to **`http://localhost:8085`**.
2. On the left tree menu, navigate to: `Metrics` -> `devops` -> `servers` -> `production`.
3. Click on `cpu` -> `usage` or `memory` -> `usage`. A graph plots on the right screen showing real-time CPU/Memory spikes!
4. **📸 Screenshot #5 (Graphite Metrics):** Take a screenshot of the Graphite dashboard showing the active line graph.

---

### 📈 Visualizing Grafana Dashboards
1. Open your browser to **`http://localhost:3000`**.
2. Login with Username: `admin` and Password: `admin` (skip password change if prompted).
3. **Configure Graphite Data Source:**
   - Click **Connections** (or Configuration wheel icon ⚙️) -> **Data Sources** -> **Add data source**.
   - Select **Graphite**.
   - In the **URL** box, type: `http://devops-graphite:80`
   - Scroll down and click **Save & Test** *(It will say "Data source is working")*.
4. **Create Dashboard:**
   - Click **Dashboards** -> **New Dashboard** -> **Add visualization**.
   - Select **Graphite**.
   - In the query box, enter: `devops.servers.production.cpu.usage`.
   - Add another panel for `devops.servers.production.memory.usage` and `devops.servers.production.http.availability`.
5. **📸 Screenshot #6 (Grafana Dashboard):** Take a screenshot of your finished Grafana dashboard showing CPU, Memory, Network, and Availability metrics.

---

### 🛡️ Visualizing Nagios Availability
1. Open your browser to **`http://localhost:8083`**.
2. Login with Username: `nagiosadmin` and Password: `nagios`.
3. Click on **Hosts** or **Services** on the left menu.
4. **📸 Screenshot #7 (Nagios Monitoring):** Take a screenshot showing `localhost` in the green **UP** state and HTTP service in the **OK** state.

---

## 📝 Final Checklist for Page 1 of Your PDF Report
Fill in the mandatory table on page 1 of your assignment report with:
1. **GitHub Repository Link:** `<Your GitHub URL>`
2. **Jenkins Build URL:** Include screenshots of Dashboard, Job Config, Console Output, and Successful Build.
3. **Docker Hub Repository Link:** *(Optional / Local build screenshot included)*
4. **Application URL:** `http://localhost:30080` (+ Browser screenshot)
5. **Grafana Dashboard Screenshot:** Attached in report.
6. **Nagios Monitoring Screenshot:** Attached showing UP/OK state.
7. **Graphite Metrics Screenshot:** Attached showing metrics graph.
