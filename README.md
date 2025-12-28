# JobTrackr

JobTrackr is a Django REST API project for managing and tracking platform designed to help job seekers manage applications, job postings, user profiles, track statuses, and analyze progress.
The backend is containerized using Docker, Swagger and uses MySQL as the database.
Project Status: 🎉 Backend Complete
Live Demo: [Coming Soon]

## Tech Stack
- Backend: Python, Django, Django REST Framework
- Frontend: HTML, CSS, JavaScript (planed)
- Authentication: JWT 
- Database: MySQL
- Docker & Docker Compose, Swagger/OpenAPI

  ## Features

- Recruiter job management (create, update, soft delete)
- Job listing and search
- User profile management
- Role-based permissions
- Dockerized development setup

## Project Workflow
This project follows an Agile sprint-based development approach with feature branches and continuous Git integration.

## Sprint Plan
- Sprint 0: Project setup & planning
- Sprint 1: Authentication system
- Sprint 2: Job application core module
- Sprint 3: Search, filter & pagination
- Sprint 4: Frontend integration (Planned)
- Sprint 5: Analytics dashboard
- Sprint 6: Security & optimization
- Sprint 7: Deployment & documentation (Planned)

  ## Project Structure
jobtrackr/
├── api/v1/              # API endpoints and versioning
├── applications/        # Job application models and logic
├── auth_app/           # Authentication system (JWT)
├── backend/            # Core Django settings
├── core/               # Shared utilities and base classes
├── jobs/               # Job-related functionality
├── profiles/           # User profile management
├── Dockerfile          # Docker configuration
├── docker-compose.yml  # Multi-container orchestration
├── manage.py           # Django management script
└── requirements.txt    # Python dependencies

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



