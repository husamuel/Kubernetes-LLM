# 🤖 LLM Kubernetes Infrastructure

A production-ready microservices infrastructure for serving Large Language Models with automated CI/CD, security scanning, and comprehensive monitoring. Built with Kubernetes, AWS, and modern DevOps practices.

[![Kubernetes](https://img.shields.io/badge/Kubernetes-326CE5?style=for-the-badge&logo=kubernetes&logoColor=white)](https://kubernetes.io/)
[![AWS](https://img.shields.io/badge/AWS-FF9900?style=for-the-badge&logo=amazon-aws&logoColor=white)](https://aws.amazon.com/)
[![Terraform](https://img.shields.io/badge/Terraform-7B42BC?style=for-the-badge&logo=terraform&logoColor=white)](https://www.terraform.io/)
[![Docker](https://img.shields.io/badge/Docker-2496ED?style=for-the-badge&logo=docker&logoColor=white)](https://www.docker.com/)
[![ArgoCD](https://img.shields.io/badge/ArgoCD-EF7B4D?style=for-the-badge&logo=argo&logoColor=white)](https://argoproj.github.io/cd/)

---

## 📋 Table of Contents

- [Overview](#overview)
- [Architecture](#architecture)
- [Tech Stack](#tech-stack)
- [How I Built This](#how-i-built-this)
- [Features](#features)
- [Getting Started](#getting-started)
- [Screenshots](#screenshots)

---

## 🎯 Overview

This project implements a complete infrastructure for serving Large Language Models using microservices. The system handles LLM inference requests through an API Gateway, processes them with GPT-2 Medium, and automatically stores all interactions in MongoDB.

**The Flow:**
1. Client sends request to API Gateway
2. Gateway forwards to LLM Service (GPT-2 Medium)
3. LLM generates response
4. Response goes back to client + Storage Service saves everything to MongoDB

Everything runs on Kubernetes (K3s), with full CI/CD automation, security scanning, and monitoring.

---

## 🏗️ Architecture

```
Client Request
      ↓
┌─────────────┐
│ API Gateway │ (FastAPI)
└──────┬──────┘
       ↓
┌─────────────┐
│ LLM Service │ (GPT-2 Medium)
└──────┬──────┘
       ↓
   Response → Client
       +
   Storage Service → MongoDB
```
---

## 🛠️ Tech Stack

**Application:**
- FastAPI (Python) - API Gateway
- GPT-2 Medium - Language Model
- MongoDB - Database

**Infrastructure:**
- Kubernetes (K3s)
- AWS (ECR, S3, VPC, IAM)
- Terraform - Infrastructure as Code
- Docker - Containerization

**CI/CD & Security:**
- GitHub Actions - CI/CD Pipeline
- ArgoCD - GitOps Deployment
- Trivy - Vulnerability Scanning
- Cosign - Image Signing

**Monitoring:**
- Prometheus - Metrics
- Grafana - Dashboards

---

## 🚀 How I Built This

### Step 1: Built the Application 🐍

Created three microservices with FastAPI and containerized everything:

- **API Gateway**: Receives requests and routes them
- **LLM Service**: Runs GPT-2 Medium for text generation
- **Storage Service**: Saves conversations to MongoDB

Tested everything locally with docker-compose to make sure it worked before moving to the cloud.

---

### Step 2: AWS Infrastructure with Terraform ☁️

Used Terraform to provision everything on AWS:

- **ECR**: Private registry to store my Docker images
- **S3**: Bucket for security scan reports and SBOM files
- **VPC**: Isolated network for security
- **IAM**: Roles and policies for secure access

All infrastructure is code - just run `terraform apply` and everything gets created.

---

### Step 3: CI/CD Pipeline 🔄

Set up GitHub Actions to automate everything:

1. **Build** - Creates Docker images
2. **Test** - Runs tests to catch bugs
3. **Scan** - Trivy checks for vulnerabilities
4. **SBOM** - Generates software bill of materials
5. **Push** - Uploads images to ECR
6. **Deploy** - ArgoCD automatically deploys to Kubernetes

The pipeline uploads SBOM and scan results to S3 for tracking.

---

### Step 4: GitOps with ArgoCD 🎯

Configured ArgoCD to watch my Git repository:

- Any change I push to Git automatically updates the cluster
- ArgoCD syncs the cluster state with what's in Git
- Easy rollbacks if something breaks
- Complete audit trail of all changes

---

### Step 5: Kubernetes Deployments 🕸️

Created all the Kubernetes resources:

- **Namespaces** - Isolate resources
- **Deployments** - Run the services
- **Services (ClusterIP)** - Internal networking
- **Ingress** - External access with NGINX
- **Secrets** - Store sensitive data like DB passwords
- **ConfigMaps** - Application configuration

---

### Step 6: Monitoring 📊

Set up monitoring stack:

- **Prometheus** - Collects metrics from all services
- **Grafana** - Beautiful dashboards to visualize everything

Can see in real-time:
- Request rates and latencies
- LLM inference times
- MongoDB performance
- Cluster health (CPU, memory, pods)

---

### Step 7: Image Signing 🔐

Added security with Cosign:

- Every image gets signed in the CI/CD pipeline
- Kubernetes verifies signatures before deploying
- Prevents deployment of tampered or unsigned images

---

### The ECR Token Challenge 🔧

**Problem:** AWS ECR tokens expire every 12 hours. K3s doesn't support IAM roles, so I needed a way to keep credentials fresh.

**Solution:** Created a Kubernetes CronJob that:
- Runs every 10 hours (before the 12h expiration)
- Gets a fresh token from AWS
- Updates the Kubernetes secret
- Keeps everything working 24/7

Simple but effective!


---

## 🚀 Getting Started

### Local Development

```bash
# Clone the repo
git clone https://github.com/yourusername/llm-kubernetes-infrastructure.git
cd llm-kubernetes-infrastructure

# Start services locally
docker-compose up --build

# Test the API
curl -X POST http://localhost:8000/api/v1/inference \
  -H "Content-Type: application/json" \
  -d '{"prompt": "What is Kubernetes?", "max_length": 100}'
```



## 📊 Screenshots

### ArgoCD Dashboard
*[Add screenshot of ArgoCD showing healthy applications]*

### Grafana Monitoring
*[Add screenshot of Grafana dashboards]*

### GitHub Actions Pipeline
*[Add screenshot of successful CI/CD run]*

### Kubernetes Cluster
*[Add screenshot of running pods]*

---

## 🔒 Security Features

- Container vulnerability scanning with Trivy
- Image signing with Cosign
- SBOM generation for compliance
- Kubernetes secrets for sensitive data
- Network isolation with VPC
- IAM least privilege policies
- Automated security artifact storage in S3

---

## 📈 Monitoring

**What I Track:**
- API request rate and latency
- LLM inference time
- MongoDB operations
- CPU and memory usage
- Pod health and restarts

**Tools:**
- Prometheus for metrics collection
- Grafana for visualization
- Custom dashboards for each service

---

## 🎯 What I Learned

- Building production-ready microservices
- Infrastructure as Code with Terraform
- Kubernetes orchestration and networking
- CI/CD pipeline automation
- GitOps methodology with ArgoCD
- Container security and image signing
- Prometheus metrics and Grafana dashboards
- Problem solving (like the ECR token challenge!)
