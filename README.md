# 🧹 Cleaning Service Microservices Platform

This project is a **production-style, cloud-native microservices application** designed to demonstrate **real-world DevOps, Cloud, and Security best practices**.

It covers the **full lifecycle**:

* Local development with Docker Compose
* Containerization with Docker
* Kubernetes orchestration
* AWS EKS provisioning with Terraform
* Image management with Amazon ECR
* CI/CD with Jenkins
* Security with RBAC, NetworkPolicies, and Secrets

> 🎯 **Goal**: Show how a modern microservices application is built, secured, deployed, and operated in AWS.

---

## 🏗 Architecture Overview

```
┌──────────────┐
│   Clients    │
└──────┬───────┘
       │
┌──────▼───────┐
│ API Gateway  │  (Nginx)
└──────┬───────┘
       │
┌──────▼───────────────────────────────┐
│          Kubernetes (EKS)             │
│                                      │
│  ┌────────┐ ┌────────┐ ┌────────┐   │
│  │ User   │ │Booking │ │Worker  │   │
│  │Service │ │Service │ │Service │   │
│  └────────┘ └────────┘ └────────┘   │
│            ┌────────┐               │
│            │Payment │               │
│            │Service │               │
│            └────────┘               │
└──────────────────────────────────────┘

Images stored in Amazon ECR
Infrastructure provisioned by Terraform
CI/CD orchestrated by Jenkins
```

---

## 📁 Repository Structure

```
CLEANING-SERVICE-APP/
│
├── api-gateway/           # Nginx reverse proxy
├── user-service/          # User management microservice
├── booking-service/       # Booking microservice
├── worker-service/        # Cleaner/worker microservice
├── payment-service/       # Payment microservice
│
├── k8s/                   # Kubernetes manifests
│   ├── namespace.yaml
│   ├── secrets.yaml
│   ├── rbac.yaml
│   ├── network-policy.yaml
│   ├── api-gateway.yaml
│   ├── user-service.yaml
│   ├── booking-service.yaml
│   ├── worker-service.yaml
│   └── payment-service.yaml
│
├── terraform/             # Infrastructure as Code (EKS, VPC)
│   ├── providers.tf
│   ├── vpc.tf
│   ├── eks.tf
│   ├── iam.tf
│   ├── variables.tf
│   └── outputs.tf
│
├── ansible/               # Configuration management (Jenkins, EC2)
│   ├── inventory/
│   ├── playbooks/
│   └── roles/
│
├── docker-compose.yml     # Local development
├── Jenkinsfile            # CI/CD pipeline
├── .gitignore
└── README.md
```

---

## 🚀 Local Development (Docker Compose)

### Prerequisites

* Docker Desktop
* Docker Compose v2

### Run Locally

```bash
docker compose up --build
```

Services will be available via the API Gateway.

---

## 🐳 Containerization

Each microservice:

* Has its own `Dockerfile`
* Is independently buildable
* Communicates over internal networking

Example build:

```bash
docker build -t user-service ./user-service
```

---

## 📦 Amazon ECR (Image Registry)

Images are pushed to **Amazon Elastic Container Registry**.

Flow:

1. Jenkins builds Docker images
2. Jenkins authenticates to ECR
3. Images are tagged and pushed
4. EKS pulls images securely via IAM

---

## ☸ Kubernetes (EKS)

### What Runs in Kubernetes

* Deployments for each microservice
* ClusterIP Services for internal communication
* Secrets for sensitive values
* NetworkPolicies for traffic control
* RBAC for least privilege access

### Deploy to Cluster

```bash
kubectl apply -f k8s/
```

---

## 🔐 Security Model

### Kubernetes Security

* **Namespaces**: logical isolation
* **RBAC**: least-privilege access
* **Secrets**: no plaintext credentials
* **NetworkPolicies**: zero-trust networking

### AWS Security

* IAM Roles for Service Accounts (IRSA)
* No static AWS keys in containers
* Private subnets for worker nodes

---

## 🏗 Infrastructure with Terraform

Terraform provisions:

* VPC (public & private subnets)
* NAT Gateway
* EKS Cluster
* Managed Node Groups

### Deploy Infrastructure

```bash
cd terraform
terraform init
terraform apply
```

---

## 🔄 CI/CD with Jenkins

### Pipeline Stages

1. Checkout source code
2. Build Docker images
3. Push images to ECR
4. Deploy to EKS using kubectl

### Jenkinsfile Location

```
/Jenkinsfile
```

---

## 🤖 Where Ansible Fits

Ansible is used for:

* Jenkins server bootstrapping
* EC2 hardening
* Tool installation (Docker, kubectl, awscli)
* Day-2 operations (patching, config changes)

Terraform **creates** servers.
Ansible **configures** servers.

---

## 🎯 Interview Walkthrough Summary

> “This project demonstrates how I design and operate a secure microservices platform using Docker, Kubernetes, Terraform, Jenkins, and Ansible on AWS. Infrastructure is declarative, deployments are automated, and security is enforced at every layer.”

---

## 🧠 Skills Demonstrated

* AWS (EKS, ECR, IAM, VPC)
* Kubernetes (Deployments, Services, RBAC)
* Docker & Microservices
* Terraform (IaC)
* Jenkins (CI/CD)
* Ansible (Configuration Management)
* Cloud Security & Best Practices

---

## 📌 Future Enhancements

* Helm charts
* HPA & Cluster Autoscaler
* Prometheus & Grafana
* AWS ALB Ingress Controller
* WAF integration

---

## 👤 Author

**Betrand Mbah**
Cloud / DevOps / Security Engineer
