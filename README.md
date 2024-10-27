
# Simple Vulnerable Web Application

This repository contains a simple, intentionally vulnerable web application designed for penetration testing and cybersecurity training. The application is packaged in a Docker container for easy deployment. **Use this application only in a controlled environment, as it contains known security vulnerabilities.**

## Table of Contents

- [Features](#features)
- [Prerequisites](#prerequisites)
- [Installation](#installation)
- [Usage](#usage)
- [Stopping the Application](#stopping-the-application)
- [Troubleshooting](#troubleshooting)

## Features

This web application includes vulnerabilities for training purposes, including:
- Cross-Site Scripting (XSS)
- Cross-Site Request Forgery (CSRF)
- Server-Side Request Forgery (SSRF)
- Remote Code Execution (RCE)

## Prerequisites

- [Docker](https://docs.docker.com/get-docker/) installed on your system.

## Installation

1. **Pull the Docker Image**

   Run the following command to pull the Docker image from Docker Hub:

   ```bash
   docker pull yourusername/simple_vuln_web_app:latest
   ```

2. **Run the Docker Container**

   Use the following command to start the container with a specific name (`t-code-now`), mapping it to port 5000 on your machine:

   ```bash
   sudo docker run -d -p 5000:5000 --name t-code-now yourusername/simple_vuln_web_app:latest
   ```

   This command will:
   - Start the container in detached mode (`-d`).
   - Map port 5000 on your host to port 5000 in the container.
   - Assign the container the name `t-code-now` for easy identification.

## Usage

Once the container is running, you can access the web application in your browser:

- **Local Access**: [http://127.0.0.1:5000](http://127.0.0.1:5000)
- **Network Access** (replace `<host_ip>` with your host's IP address): `http://<host_ip>:5000`

### Verifying the Container

To confirm the container is running, you can check with:

```bash
sudo docker ps
```

You should see `t-code-now` in the `NAMES` column if the container is running correctly.

## Stopping the Application

To stop the application, run:

```bash
sudo docker stop t-code-now
```

To remove the container after stopping it, use:

```bash
sudo docker rm t-code-now
```

## Troubleshooting

- **Error: Name `t-code-now` is already in use**  
  If you see an error stating that `t-code-now` is already in use, it means a container with this name exists (possibly from a previous run). Remove it with:

  ```bash
  sudo docker rm t-code-now
  ```

- **Container Exits Immediately**  
  If the container stops right after starting, check the logs to troubleshoot the issue:

  ```bash
  sudo docker logs t-code-now
  ```

---

## Disclaimer

This application is for **educational and testing purposes only**. Do not deploy this application on production environments or networks containing sensitive data. Misuse of this software could lead to data breaches or other security incidents.
