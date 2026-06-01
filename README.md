# Cloud Journey 2026

Documenting my journey to becoming a Cloud Engineer.

---

## Day 1
- Set up development environment (VS Code, Git, Ubuntu WSL)
- Learned cloud basics (IaaS, PaaS, SaaS)

## Day 2
- Learned Linux fundamentals
- Practiced file operations (touch, cp, mv, rm)
- Understood file permissions (chmod, rwx)

## Day 3
- Practiced advanced Linux navigation
- Managed processes (ps, kill, top)
- Initialized Git and pushed project to GitHub

## Day 4 — Networking Basics

### What I Learned
- IP address (public vs private)
- DNS and how domain names map to IPs
- Ports and how services run on same server
- HTTP vs HTTPS (encryption, security)
- How a website loads step-by-step

### Hands-on Commands
- ping → checked connectivity and latency
- nslookup → resolved domain to IP
- traceroute → observed network path (hops)

### Key Understanding
When accessing a website, data does not go directly from client to server. 
It travels through multiple routers (hops), and tools like traceroute help visualize this path.

### Problems Faced
- Confusion in traceroute output
- Weak understanding of ports initially

### Fix
Rebuilt concepts and understood real meaning with examples

---

## Day 5 — Bash Automation & Monitoring

### What I Learned
- **Bash Scripting:** Using arrays `()` and `for` loops to handle multiple tasks at once.
- **Advanced Logic:** Implementing `if/else` conditions based on command success or failure.
- **HTTP Deep-Dive:** Understanding the difference between 200 (Success), 301/302 (Redirects), and 403 (Forbidden).
- **Domain Verification:** Learning to use `${website#https://}` to strip prefixes and compare URLs for security.

### Hands-on Tasks
- **The "Truth" Script:** Built a monitor that follows redirects (`curl -L`) and verifies if the final destination matches the source.
- **Log Management:** Used `>>` (append) to create a persistent history of server health.

### Key Understanding
Monitoring isn't just about checking if a site is "on." It's about verifying the **integrity** of the connection. If a site redirects somewhere unexpected, the system should flag it as a failure.

---

## 🛠 Projects Master List
### 1. Website Uptime Monitor 
- **Location:** `Projects/Website-Monitor/src/monitor.sh`
- **Tech:** Bash, Curl, Linux Redirection
- **Features:** - Multi-site monitoring via arrays.
    - Detection of ISP hijacking/malicious redirects.
    - Automated logging with timestamps.
- **Status:** ✅ Complete
---

## Day 6 — Automation Concepts (Theory)

- **Automation:** Converting manual tasks into self-running processes  
- **Scheduling (cron):** Running tasks automatically at fixed intervals using time-based patterns  
- **Background Execution:** Systems run independently without user interaction  
- **Persistence:** Continuous execution over time builds meaningful monitoring data  
- **Cron:** A Linux time-based scheduler used to automate tasks via crontab entries  
- **Cron Format:** `* * * * * command_to_execute` (minute hour day month weekday)  
- **Example:** `*/5 * * * * /path/to/script.sh` → runs every 5 minutes  
- **Key Understanding:** Manual execution = testing, Scheduled execution = real-world usage, Monitoring must be continuous, Scheduling converts scripts into systems  
- **What I Realized:** A script alone has limited value, automation is essential in cloud/DevOps workflows, and continuous logging over time provides meaningful insights

## Day 7 — Cron Automation

- Automated monitor using cron (runs every 5 minutes)
- Fixed relative path bug — learned why absolute paths matter in automated systems
- Monitor now logs continuously without manual execution
- Status: ✅ Complete

## Day 8 — Docker Basics

- Understood difference between images and containers
- Ran Ubuntu 26.04 container from local machine running 24.04
- Learned immutable infrastructure — containers are disposable, images are permanent
- Practiced container lifecycle: run, exec, exit, delete
- Status: ✅ Complete

## Day 9 — Dockerfile + Containerizing Website Monitor

- Wrote first Dockerfile from scratch
- Built custom image: website-monitor
- Debugged path issues inside container
- Ran website monitor successfully inside Docker
- Learned layer caching — unchanged layers reuse saved results
- Status: ✅ Complete

## Day 10 — Docker Volumes: Persistent Logs

- Understood why containers lose data on deletion
- Connected machine logs folder to container using bind mount
- Proved persistence — container deleted, logs survived
- Learned difference: without volume = logs die, with volume = logs persist
- Status: ✅ Complete

## Day 11 — Environment Variables

- Removed hardcoded websites from monitor script
- Added SITES environment variable with default fallback
- Tested same image with 3 different site configurations — zero rebuilds
- Learned: configuration lives outside the image, not inside it
- CODE=000 = curl couldn't connect, site unreachable
- Status: ✅ Complete

## Day 12 — Docker Compose

- Replaced long docker run commands with docker-compose.yml
- Defined services, environment variables, volumes in one file
- Ran monitor with single command: docker-compose up
- Learned -d flag for detached/background mode
- Learned docker-compose down removes containers and network, not volumes
- Status: ✅ Complete

## Day 13 — GitHub Actions: CI Pipeline

- Created .github/workflows/ci.yml
- Pipeline triggers automatically on every push to main
- Steps: checkout code → build Docker image → run monitor
- First pipeline ran successfully — green checkmark ✅
- Learned: CI automates build and test, no manual steps needed
- Status: ✅ Complete

## Day 14/15 — Azure Deployment

- Installed Azure CLI and logged in
- Created Azure Container Registry (arifmonitorregistry)
- Pushed Docker image to ACR
- Deployed monitor to Azure Container Instances
- Fixed stdout logging with tee for cloud log capture
- Monitor ran in Microsoft datacenter — Central India
- Status: ✅ Complete

## Day 16 — Full CI/CD Pipeline

- Connected GitHub Actions to Azure via Service Principal
- Added 4 GitHub Secrets for secure credential storage
- Pipeline auto-builds, pushes to ACR, and redeploys on every push
- Zero manual deployment steps
- Status: ✅ Complete

## Day 17 — Public Status Page

- Built Python web server to display monitor results
- Two containers sharing logs via Docker named volume
- Monitor writes → status page reads → browser displays
- Accessible at http://localhost:8080
- Status: ✅ Complete

## Day 18 — Azure Deployment: Public Status Page

- Created Azure Storage Account and File Share
- Deployed monitor container with Azure File Share mounted at /app/logs
- Deployed status page container with same File Share mounted
- Both containers share logs via Azure File Share
- Status page live at: http://arif-status-page.centralindia.azurecontainer.io
- Status: ✅ Complete

## Day 19 — Status Page UI Upgrade

- Added green/red color indicators for UP/DOWN status
- Added auto-refresh every 30 seconds
- Redeployed to Azure Container Instances
- Live at: http://arif-status-page.centralindia.azurecontainer.io
- Status: ✅ Complete

## Day 20 — Interactive URL Checker

- Added input form to status page
- Users can type any URL and get instant UP/DOWN result
- Fixed URL encoding with urllib.parse.unquote
- Installed curl in Python container via Dockerfile
- Live at: http://arif-status-page.centralindia.azurecontainer.io
- Status: ✅ Complete

---

## Folder Structure

```
Cloud-2026/
├── .github/
│   └── workflows/
│       └── ci.yml
├── Certification/
├── Daily-Logs/
│   ├── Day1.txt
│   └── Day2.txt
├── Linux-Practice/
├── Notes/
│   └── Day4.md
├── Projects/
│   ├── Project1/
│   ├── Status-Page/
│   │   ├── Dockerfile
│   │   └── app.py
│   └── Website-Monitor/
│       ├── Dockerfile
│       ├── docker-compose.yml
│       ├── logs/
│       └── src/
│           └── monitor.sh
└── README.md
```
## Goal
To become a job-ready Cloud Engineer by Dec 2026
