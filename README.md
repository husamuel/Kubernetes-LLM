# LLM Kubernetes Infrastructure

A microservices infrastructure for serving Large Language Models with automated CI/CD, GitOps, security scanning, and monitoring. Built with Kubernetes, AWS, and DevOps best practices.

[![Kubernetes](https://img.shields.io/badge/Kubernetes-326CE5?style=for-the-badge&logo=kubernetes&logoColor=white)](https://kubernetes.io/)
[![AWS](https://img.shields.io/badge/AWS-FF9900?style=for-the-badge&logo=amazon-aws&logoColor=white)](https://aws.amazon.com/)
[![Terraform](https://img.shields.io/badge/Terraform-7B42BC?style=for-the-badge&logo=terraform&logoColor=white)](https://www.terraform.io/)
[![Docker](https://img.shields.io/badge/Docker-2496ED?style=for-the-badge&logo=docker&logoColor=white)](https://www.docker.com/)
[![ArgoCD](https://img.shields.io/badge/ArgoCD-EF7B4D?style=for-the-badge&logo=argo&logoColor=white)](https://argoproj.github.io/cd/)


## 📋 Table of Contents

- [Overview](#overview)
- [Architecture](#architecture)
- [Tech Stack](#tech-stack)
- [How I Built](#how-i-built)
- [Getting Started](#getting-started)



## Overview

This project implements a complete infrastructure for serving Large Language Models using microservices. The system handles LLM inference requests through an API Gateway, processes them with GPT-2 Medium, and stores all interactions in MongoDB.

**The Flow:**
1. Client sends request to API Gateway
2. Gateway forwards to LLM Service (GPT-2 Medium)
3. LLM generates response
4. Response goes back to client + Storage Service saves to MongoDB

Everything runs on Kubernetes (K3s), with full CI/CD automation, security scanning, and monitoring.


## Architecture



## Tech Stack

**Application:**
- FastAPI (Python) - API Gateway & Services
- GPT-2 Medium - Language Model
- MongoDB - Database

**Infrastructure:**
- Kubernetes (K3s) - Container Orchestration
- AWS (ECR, S3, VPC, IAM) - Cloud Resources
- Terraform - Infrastructure as Code
- Docker - Containerization

**CI/CD & Security:**
- GitHub Actions - CI/CD Pipeline
- ArgoCD - GitOps Deployment
- Trivy - Vulnerability Scanning
- GitLeaks - Secret Detection
- Anchore - SBOM Generation
- Cosign - Image Signing
- Kyverno - Policy Enforcement

**Monitoring:**
- Prometheus - Metrics Collection
- Grafana - Dashboards & Visualization


## How I Built This

### 1. Setting Up the Lab

I didn't want to use my personal computer or pay for cloud services, so I grabbed an old computer I had at home, installed Ubuntu Server on it (headless to save resources), and turned it into my lab environment. It's been running everything from development to production.

<img src="https://github.com/user-attachments/assets/49ee56b5-c401-4c02-9349-240980679050" alt="Home Lab Setup" width="600"/>

### 2. Building the Application

I went with microservices where each part runs independently and communicates through REST APIs. This made sense because I could scale services separately, deploy them independently, and keep the codebase organized.

The stack is straightforward - Python with FastAPI for the servers, GPT-2 Medium as the LLM, and MongoDB for storage. Each service runs in its own Docker container. The flow works like this: gateway receives a POST to `/generate` with a prompt, processes it as JSON, forwards to the LLM service which generates a response, sends it back to the gateway and then to the client. Meanwhile, it also sends the data to the storage API that persists everything in MongoDB.

### 3. Container Registry and Infrastructure

After containerizing the services, I needed somewhere to store the images. Used AWS ECR and provisioned everything with Terraform - ECR repositories for each service, S3 buckets for SBOM reports, VPC, and IAM roles with proper policies. Infrastructure as code lets me version everything, reproduce it easily, and track all changes.

### 4. CI Pipeline

GitHub Actions handles the CI process. Every push triggers a build and push of Docker images to ECR (authentication via GitHub secrets). The pipeline runs GitLeaks to catch any exposed secrets, Trivy scans for vulnerabilities (results stored as artifacts), generates SBOM reports that get uploaded to S3, and signs all images with Cosign for integrity verification.

### 5. CD with ArgoCD

For continuous deployment, ArgoCD watches the Git repository and automatically syncs changes to the cluster. This approach speeds up development significantly - automatic deployments, faster health checks, easier debugging, and proper GitOps practices.

<img src="https://github.com/user-attachments/assets/405f5158-b803-46ee-a4a6-30d075d7af8c" alt="ArgoCD Dashboard" width="800"/>

### 6. Kubernetes Cluster

Originally wanted to use EKS Anywhere but it requires 16GB RAM minimum. My machine only has 3.8GB, so that wasn't an option. Switched to K3s instead, which is much lighter and perfect for resource-constrained environments.

Organized the cluster into namespaces: `argocd`, `gateway`, `monitoring`, `llm`, `storage`, `kyverno`, and `ingress-nginx`. The gateway uses Ingress NGINX to expose the application externally, ClusterIP services handle internal pod communication, and I configured horizontal pod autoscaling for the APIs and LLM based on resource usage. MongoDB runs as a StatefulSet with vertical scaling for data persistence.

Added Kyverno policies to verify image signatures - only signed images can run in the cluster. One challenge with ECR is token expiration, so I wrote a cronjob that runs every 10 hours to generate new authentication tokens and update the Kubernetes secrets automatically.

### 7. Monitoring

Deployed a monitoring stack using Helm with Prometheus and Grafana. Set up custom dashboards to track resource usage, application performance, and overall cluster health. This visibility was crucial for identifying bottlenecks and optimization opportunities.

<img src="https://github.com/user-attachments/assets/23882531-ca3b-41b7-99ba-d37a48ad5428" alt="Grafana Dashboard" width="800"/>

### 8. Optimizing Everything

Analyzing the Grafana dashboards revealed the cluster was struggling with RAM usage. Surprisingly, Prometheus itself was the biggest consumer. Adjusted the scrape interval from 5 seconds to 2 minutes (reasonable for a learning project) which significantly reduced memory consumption. Also defined resource limits for all pods, optimized Docker images using multi-stage builds and Alpine base images, and cleaned up unnecessary components.

### 9. Security

Security was a priority from the start. Implemented multiple layers: GitLeaks prevents secrets in code, Trivy scans catch vulnerabilities in images and dependencies, SBOM reports document all components, IAM follows least privilege principles, Kubernetes secrets store credentials securely, and Cosign signatures verify image integrity. Kyverno policies enforce that only verified signed images can execute in the cluster.

### 10. Wrapping Up

This project demonstrated that you can build production-grade cloud-native infrastructure even with limited hardware. The main challenges were working within the 3.8GB RAM constraint, managing ECR authentication in Kubernetes, and optimizing resource usage across the board. Getting a complete CI/CD pipeline, functional K3s cluster, comprehensive monitoring, and proper DevSecOps practices running smoothly on old hardware made it all worthwhile.

---

## Getting Started

### Prerequisites

- Docker & Docker Compose
- Kubernetes cluster (K3s recommended)
- AWS Account (for ECR)
- Terraform

### Deploying to Kubernetes

```bash
# Setup AWS credentials
export AWS_ACCESS_KEY_ID="your-access-key"
export AWS_SECRET_ACCESS_KEY="your-secret-key"

# Provision infrastructure with Terraform
cd terraform
terraform init
terraform apply

# Deploy to K3s cluster
kubectl apply -f k8s/

# Access via Ingress
curl -X POST http://your-ingress-url/generate \
  -H "Content-Type: application/json" \
  -d '{"prompt": "Hello world"}'
```
