# JobTrackr

JobTrackr is a Django REST API project for managing and tracking platform designed to help job seekers manage applications, job postings, user profiles, track statuses, and analyze progress.
The backend is containerized using Docker, Swagger and uses MySQL as the database.
> **Project Status:** 🎉 Backend Complete
---
## 🛠 Tech Stack

| Layer | Technology |
| :--- | :--- |
| **Backend** | Python, Django, Django REST Framework |
| **Database** | MySQL |
| **Auth** | JWT (JSON Web Tokens) |
| **Container** | Docker & Docker Compose |
| **API Docs** | Swagger / OpenAPI |

---

  ## Features

- Recruiter job management (create, update, soft delete)
- Job listing and search
- User profile management
- Role-based permissions
- Dockerized development setup

## Project Workflow
This project follows an Agile sprint-based development approach with feature branches and continuous Git integration.

##  Sprint Plan (Agile)

- [x] **Sprint 0:** Project setup & planning
- [x] **Sprint 1:** Authentication system (JWT)
- [x] **Sprint 2:** Job application core module
- [x] **Sprint 3:** Search, filter & pagination
- [ ] **Sprint 4:** Frontend integration (Planned)
- [ ] **Sprint 5:** Analytics dashboard
- [ ] **Sprint 6:** Security & optimization
- [ ] **Sprint 7:** Deployment & documentation

##  Project Structure

```text
jobtrackr/
├── api/v1/          # API endpoints and versioning
├── applications/    # Job application models
├── auth_app/        # Authentication system
├── backend/         # Core Django settings
├── core/            # Shared utilities
├── jobs/            # Job functionality
├── profiles/        # User management
├── Dockerfile       # Docker config
└── docker-compose.yml

## How to Run Locally

```bash
git clone https://github.com/your-username/jobtrackr.git
cd jobtrackr

```bash
python -m venv env
env\Scripts\activate
pip install -r requirements.txt
python manage.py runserver

## Create .env File
DEBUG=True
SECRET_KEY=your django key
ALLOWED_HOSTS=127.0.0.1,localhost

DB_NAME=jobtrackr_db
DB_USER=jobtrackr_user
DB_PASSWORD=strongpassword
DB_HOST=localhost
DB_PORT=3306

## Create database
```bash
CREATE DATABASE jobtrackr_db;

## Run Migrations
```bash
python manage.py makemigrations
python manage.py migrate
python manage.py runserver

### Run Project Using Docker
create .env.docker File
DEBUG=True
SECRET_KEY=django-insecure-change-this
ALLOWED_HOSTS=127.0.0.1,localhost

DB_NAME=jobtrackr_db
DB_USER=jobtrackr_user
DB_PASSWORD=strongpassword
DB_HOST=db
DB_PORT=3306

## Build and Start Containers
docker compose up --build
## Run Migrations (Docker)
docker compose exec backend python manage.py migrate

API: http://localhost:8000/api/v1/
Swagger Documentation: http://127.0.0.1:8000/api/docs/



