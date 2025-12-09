# LLM Kubernetes Infrastructure

Microservices infrastructure for serving LLMs with API Gateway, request processing, automatic MongoDB storage, and complete CI/CD pipeline. All running on Kubernetes in AWS with Terraform.

## Description

This project implements a complete and scalable infrastructure for serving a Large Language Model using microservices architecture. The flow works like this: an API Gateway receives client requests and forwards them to the LLM service that processes and generates responses. When the response goes back to the client, simultaneously a storage service saves the entire interaction in MongoDB for history and analysis.

The infrastructure runs on Kubernetes managed by EKS Anywhere, with all services containerized in Docker. The cloud infrastructure was fully provisioned on AWS using Terraform, including VPC for network isolation, S3 for storing security scan results, and ECR as a private image registry.

The project features an automated CI/CD pipeline that builds images on every push, runs integration tests, performs vulnerability scans, and automatically pushes approved images to ECR. Everything designed to be scalable, secure, and easy to maintain.

#1 Criei a aplicação com python usei a bilbitoeca fastAPI para o llm usei o modelo gpt2-medium criei o seviço que vai enviar os dados para a DB e cria la configuerei os docker files e testei localmente para assegurar que estava tudo bem

#2 Criei os meus serviços na aws usando terraform criei o ECR para armazenas as imagens da minha aplicação e o S3 para guardar os SBOM e VPC e IAM

#3 Criei pipeline com github actions que conecta à minha conta aws, dá build push scan com trivy das imagens e gera SBOM que envia para o S3

#4 Configurei o AegoCD para ouvir o meu repositorio e atualizar o meu cluster à medida que ia construindo

#5 Criação dos deploymets dos serviços namespaces, ingress, clusterip, secrets

#6 monitoramento do cluster com prometheus e grafana

#7 Assinatura de imagens com COSIGN

O AWS ECR só permite pull de imagens privadas usando tokens temporários de 12h como estou a usar o k3s não consigo fazer um iam role para o meu cluster então criei um cronjob que atualiza o token de 10 em 10h apartir do aws cli 
