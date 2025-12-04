# LLM Kubernetes Infrastructure

Microservices infrastructure for serving LLMs with API Gateway, request processing, automatic MongoDB storage, and complete CI/CD pipeline. All running on Kubernetes in AWS with Terraform.

## Description

This project implements a complete and scalable infrastructure for serving Large Language Models using microservices architecture. The flow works like this: an API Gateway receives client requests and forwards them to the LLM service that processes and generates responses. When the response goes back to the client, simultaneously a storage service saves the entire interaction in MongoDB for history and analysis.

The infrastructure runs on Kubernetes managed by EKS Anywhere, with all services containerized in Docker. The cloud infrastructure was fully provisioned on AWS using Terraform, including VPC for network isolation, S3 for storing security scan results, and ECR as a private image registry.

The project features an automated CI/CD pipeline that builds images on every push, runs integration tests, performs vulnerability scans, and automatically pushes approved images to ECR. Everything designed to be scalable, secure, and easy to maintain.
