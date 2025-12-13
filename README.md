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
