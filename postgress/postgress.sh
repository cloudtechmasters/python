#!/bin/bash

# Add the Helm repository for PostgreSQL
helm repo add bitnami https://charts.bitnami.com/bitnami

# Update the Helm repositories
helm repo update

# Set strong username and password
POSTGRES_USERNAME="your_username"
POSTGRES_PASSWORD="your_strong_password"

# Install PostgreSQL using Helm with the provided credentials
helm install my-postgres bitnami/postgresql \
  --set postgresqlUsername=$POSTGRES_USERNAME \
  --set postgresqlPassword=$POSTGRES_PASSWORD \
  --set postgresqlDatabase=mydatabase

# Wait for the PostgreSQL deployment to be ready
kubectl wait --for=condition=ready pod -l app=my-postgres --timeout=300s

echo "PostgreSQL installed successfully with strong credentials!"
