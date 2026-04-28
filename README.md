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

## Folder Structure

```
Cloud-2026/
├── Notes/
├── Projects/
├── Certificates/
└── Daily-Logs/
```
## Goal
To become a job-ready Cloud Engineer by Dec 2026
