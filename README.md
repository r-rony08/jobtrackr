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
```
### Create a .env file in the root directory
```ini
DEBUG=True
SECRET_KEY=your django key password
ALLOWED_HOSTS=127.0.0.1,localhost

# Database Settings
DB_NAME=jobtrackr_db
DB_USER=jobtrackr_user
DB_PASSWORD=your_local_password
DB_HOST=localhost
DB_PORT=3306
```
** Create database
```bash
CREATE DATABASE jobtrackr_db;
```
```bash
# Activate Virtual Environment
python -m venv env

# On Windows:
env\Scripts\activate

# Install Dependencies
pip install -r requirements.txt

# Run Migrations and Start Server
python manage.py migrate
python manage.py runserver
```
# API Documentation
API Root: http://localhost:8000/api/v1/
Swagger UI: http://127.0.0.1:8000/api/docs/

### Run Project Using Docker

** create .env.docker File
```ini
DEBUG=True
SECRET_KEY=your django key password
ALLOWED_HOSTS=127.0.0.1,localhost
DB_NAME=jobtrackr_db
DB_USER=jobtrackr_user
DB_PASSWORD=your_local_password
DB_HOST=db
DB_PORT=3306
```
```bash
** Build and Start Containers
docker compose up --build
** Run Migrations (Docker)
docker compose exec backend python manage.py migrate
```



