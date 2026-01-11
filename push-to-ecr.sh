#!/bin/bash

# ----------------------------
# Configuration
# ----------------------------
AWS_ACCOUNT_ID="439891535932"
AWS_REGION="us-east-1"

# List of services
SERVICES=("user-service" "booking-service" "worker-service" "payment-service" "api-gateway")

# ----------------------------
# 1️⃣ Login to ECR
# ----------------------------
echo "Logging into AWS ECR..."
aws ecr get-login-password --region $AWS_REGION | \
docker login --username AWS --password-stdin $AWS_ACCOUNT_ID.dkr.ecr.$AWS_REGION.amazonaws.com

# ----------------------------
# 2️⃣ Build, Tag, and Push Images
# ----------------------------
for SERVICE in "${SERVICES[@]}"; do
    echo "-----------------------------------------"
    echo "Building image for: $SERVICE"
    docker build -t $SERVICE ./$SERVICE

    echo "Tagging image for ECR..."
    docker tag $SERVICE:latest $AWS_ACCOUNT_ID.dkr.ecr.$AWS_REGION.amazonaws.com/$SERVICE:latest

    echo "Pushing $SERVICE image to ECR..."
    docker push $AWS_ACCOUNT_ID.dkr.ecr.$AWS_REGION.amazonaws.com/$SERVICE:latest
done

echo "-----------------------------------------"
echo "All images built and pushed successfully!"
