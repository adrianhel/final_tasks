#!/bin/bash

# Установка Java в контейнеры Airflow
echo "Installing Java in Airflow containers..."

# Установка в airflow-worker
docker-compose exec -u root airflow-worker apt-get update
docker-compose exec -u root airflow-worker apt-get install -y openjdk-11-jdk-headless

# Установка в airflow-scheduler
docker-compose exec -u root airflow-scheduler apt-get update
docker-compose exec -u root airflow-scheduler apt-get install -y openjdk-11-jdk-headless

# Установка в airflow-webserver
docker-compose exec -u root airflow-webserver apt-get update
docker-compose exec -u root airflow-webserver apt-get install -y openjdk-11-jdk-headless

echo "Java installation completed!"