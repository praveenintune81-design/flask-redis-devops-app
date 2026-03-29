# Flask + Redis Counter App

# 🚀 Flask + Redis Visitor Counter (Dockerized DevOps Project)

This project is a simple yet powerful DevOps-style application built using Flask and Redis. It demonstrates how to run a multi-container application using Docker Compose.

## 📌 Project Overview

This application tracks the number of visitors accessing the website.

Each time the page is refreshed:
- A counter increases
- The value is stored in Redis (in-memory database)

## 🧰 Tech Stack

| Component | Technology |
|----------|-----------|
| Backend | Flask (Python) |
| Database | Redis |
| Containerization | Docker |
| Orchestration | Docker Compose |

## ⚙️ How It Works

- Flask handles incoming HTTP requests
- Redis stores the visitor count
- Docker Compose runs both services together
- Services communicate using Docker internal network


## 📁 Project Structure
flask-redis-app/
├── app.py
├── requirements.txt
├── Dockerfile
├── docker-compose.yml

## ▶️ Run the Application

### Step 1: Build and Start Containers

docker-compose up --build

Step 2: Open in Browser
http://localhost

Output
🚀 DevOps Learning App
You are visitor number: 1
You are visitor number: 2

🔍 Endpoints

Route	Description
/	Visitor Counter
/health	Health Check

🧠 Key Learnings

Docker image creation
Multi-container architecture using Docker Compose
Container networking (service-to-service communication)
Environment variables usage
Redis integration with Flask

