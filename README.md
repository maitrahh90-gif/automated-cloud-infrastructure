# Automated Cloud Infrastructure & DevOps Project

## 🚀 Project Overview

This project demonstrates an Automated Cloud Infrastructure and DevOps workflow using Python, Docker, Terraform, and GitHub Actions.

The goal is to automate infrastructure provisioning, containerize a Python application, and implement CI/CD practices using GitHub Actions.

## 🛠️ Technologies Used

- **Python** – Application development
- **Docker** – Application containerization
- **Terraform** – Infrastructure as Code (IaC)
- **GitHub Actions** – CI/CD automation
- **Git & GitHub** – Version control and source code management

## 📂 Project Structure

```text
automated-cloud-infrastructure/
│
├── .github/
│   └── workflows/
│
├── app/
│
├── terraform/
│
├── Dockerfile
├── .gitignore
└── README.md
```

## ⚙️ Key Features

- Automated cloud infrastructure provisioning using Terraform.
- Containerized Python application using Docker.
- CI/CD workflow automation using GitHub Actions.
- Infrastructure as Code implementation.
- Version control and project management using GitHub.

## 🐳 Docker Setup

Build the Docker image:

```bash
docker build -t cloud-infrastructure-app .
```

Run the Docker container:

```bash
docker run cloud-infrastructure-app
```

## ☁️ Terraform Setup

Navigate to the Terraform directory:

```bash
cd terraform
```

Initialize Terraform:

```bash
terraform init
```

Validate the configuration:

```bash
terraform validate
```

Review the infrastructure plan:

```bash
terraform plan
```

## 🔄 CI/CD Pipeline

GitHub Actions is used to automate the project workflow.

The workflow configuration is maintained inside:

```text
.github/workflows/
```

## 🎯 Project Objectives

- Understand Infrastructure as Code.
- Implement Docker-based application deployment.
- Automate DevOps workflows.
- Learn CI/CD pipeline implementation.
- Build practical Cloud and DevOps engineering skills.

## 👩‍💻 Author

**Maitra Hariharagoudahalabhavi**

GitHub: [maitrahh90-gif](https://github.com/maitrahh90-gif)

---

⭐ If you find this project useful, feel free to explore the repository!
Automated Cloud Infrastructure & Containerized Python AI Service

Project Overview

This project demonstrates how to build and run a Python REST API using FastAPI and Docker, with Terraform configuration and GitHub Actions for infrastructure and CI/CD workflow automation.

Technologies Used

- Python
- FastAPI
- Docker
- Terraform
- AWS (planned deployment)
- GitHub Actions
- Git and GitHub

Project Architecture

Developer
   |
   v
GitHub Repository
   |
   v
GitHub Actions (CI/CD)
   |
   v
Python FastAPI Application
   |
   v
Docker Container
   |
   v
REST API Endpoints

Features

- REST API developed using FastAPI.
- Health-check endpoint to monitor service status.
- Demo prediction endpoint.
- Docker-based application containerization.
- Terraform configuration for AWS provider.
- GitHub Actions workflow integration.

API Endpoints

Method| Endpoint| Description
GET| "/"| Home page
GET| "/health"| Health check
POST| "/predict"| Demo prediction

The "/predict" endpoint accepts a JSON value and returns the value multiplied by 2. This is a demonstration, not a trained machine-learning model.

Run Locally

pip install -r app/requirements.txt
uvicorn app.app:app --reload

Open the API documentation:

"http://127.0.0.1:8000/docs"

Run Using Docker

Build the Docker image:

docker build -t cloud-ai-service .

Run the container:

docker run -d -p 8000:8000 --name cloud-ai-container cloud-ai-service

Terraform

Terraform configuration is maintained in the "terraform/" directory. The AWS provider is configured for the Mumbai region ("ap-south-1").

AWS infrastructure provisioning has not yet been performed.

CI/CD

GitHub Actions is configured through:

".github/workflows/ci-cd.yml"

The workflow runs automatically when the configured repository events occur.

Project Status

- FastAPI application: Completed
- Docker containerization: Completed
- Terraform provider configuration: Completed
- GitHub repository: Uploaded
- GitHub Actions workflow: Configured
- AWS deployment: Planned

Author

Maitra Hariharagouda Halabhavi

"GitHub" (https://github.com/maitrahh90-git)
