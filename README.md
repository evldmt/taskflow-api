# TaskFlow API 🚀

A modern, production-ready Task Management API built with **Django REST Framework**.
Features JWT authentication, Docker support, and comprehensive test coverage.

![Python](https://img.shields.io/badge/Python-3.11-blue)
![Django](https://img.shields.io/badge/Django-5.0-green)
![Docker](https://img.shields.io/badge/Docker-Enabled-blue)
![Tests](https://img.shields.io/badge/Tests-Passing-success)

## 🛠 Tech Stack

- **Core:** Python 3.11, Django 5, DRF
- **Database:** PostgreSQL (Production), SQLite (Dev)
- **Authentication:** JWT (SimpleJWT)
- **Documentation:** OpenAPI 3.0 (Swagger UI)
- **DevOps:** Docker, Docker Compose
- **Testing:** Pytest

## ✨ Features

- [x] **Custom User Model** (Email-based login)
- [x] **JWT Authentication** (Secure Access & Refresh tokens)
- [x] **Task Management** (CRUD operations)
- [x] **Privacy Controls** (Users see only their own tasks)
- [x] **Smart Documentation** (Auto-generated Swagger UI)
- [x] **Dockerized** (Runs with one command)

## 🚀 How to Run

### Option 1: Using Docker (Recommended)

Run the entire stack (App + DB) with a single command:

```bash
# 1. Clone repository
git clone [https://github.com/evldmt/taskflow-api.git](https://github.com/evldmt/taskflow-api.git)

# 2. Create .env file
cp .env.example .env

# 3. Run with Docker
docker-compose up --build