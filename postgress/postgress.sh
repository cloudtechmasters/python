#!/bin/bash

# Add Bitnami repository
helm repo add bitnami https://charts.bitnami.com/bitnami

# Update Helm repositories
helm repo update

# Install PostgreSQL with Helm
helm install my-postgres bitnami/postgresql

# Wait for PostgreSQL to be ready
kubectl wait --for=condition=ready pod -l app.kubernetes.io/instance=my-postgres -n default

# Get PostgreSQL credentials and connection details
export POSTGRES_PASSWORD=$(kubectl get secret --namespace default my-postgres-postgresql -o jsonpath="{.data.postgres-password}" | base64 --decode)
export POSTGRES_USERNAME=$(kubectl get secret --namespace default my-postgres-postgresql -o jsonpath="{.data.postgres-username}" | base64 --decode)
export POSTGRES_HOST=$(kubectl get svc --namespace default my-postgres-postgresql -o jsonpath="{.spec.clusterIP}")
export POSTGRES_PORT=5432

echo "PostgreSQL Username: $POSTGRES_USERNAME"
echo "PostgreSQL Password: $POSTGRES_PASSWORD"
echo "PostgreSQL Host: $POSTGRES_HOST"
echo "PostgreSQL Port: $POSTGRES_PORT"

echo "PostgreSQL has been successfully deployed."

# Clean up Helm installation (optional)
# helm uninstall my-postgres

