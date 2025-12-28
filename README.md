# JobTrackr

JobTrackr is a Django REST API project for managing and tracking platform designed to help job seekers manage applications, job postings, user profiles, track statuses, and analyze progress.
The backend is containerized using Docker, Swagger and uses MySQL as the database.
> **Project Status:** 🎉 Backend Complete
---
## 🛠 Tech Stack

| Layer | Technology |
| :--- | :--- |
| **Backend** | Python, Django, Django REST Framework |
| **Database** | MySQL, Redis |
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
- [x] **Sprint 5:** Analytics dashboard
- [x] **Sprint 6:** Security & optimization
- [ ] **Sprint 7:** Deployment & documentation (Planned)

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
```
## How to Run Locally
```bash
git clone https://github.com/your-username/jobtrackr.git
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
```bash
# Create database
CREATE DATABASE jobtrackr_db;

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
### 📌 API Endpoints
Authentication
Method	Endpoint	Description
POST	/api/v1/auth/register/	Register user
POST	/api/v1/auth/login/	Login
POST	/api/v1/auth/logout/	Logout
Jobs
Method	Endpoint	Description
GET	/api/v1/jobs/	List jobs
POST	/api/v1/jobs/	Create job
GET	/api/v1/jobs/{id}/	Job details
PUT	/api/v1/jobs/{id}/	Update job
DELETE	/api/v1/jobs/{id}/	Soft delete job
Applications
Method	Endpoint	Description
POST	/api/v1/applications/	Apply for job
GET	/api/v1/applications/	List applications
PATCH	/api/v1/applications/application/{id}/status/	Update application status

# API Documentation
API Root: http://localhost:8000/api/v1/ <br>
Swagger UI: http://127.0.0.1:8000/api/docs/

### Run Project Using Docker
```ini
** create .env.docker File
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
