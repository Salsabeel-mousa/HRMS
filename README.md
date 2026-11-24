# AI-HRMS: Django Base Setup

The Django + DRF base of the AI HR Management System: models, serializers, admin and REST APIs.
The AI agents, crews and flows come later and are not part of this project yet.

## Run it

```bash
# 1. Create and activate a virtual environment
python -m venv venv
source venv/bin/activate          # Windows: venv\Scripts\activate

# 2. Install dependencies
pip install -r requirements.txt

# 3. Configure the environment
cp example.env .env               # Windows: copy example.env .env
#    then edit .env: set SECRET_KEY and your PostgreSQL credentials
#    (create the database first, e.g. `createdb ai_hrms`)
#    No PostgreSQL? Set USE_SQLITE=True for a quick local try-out.

# 4. Create the tables and an admin user
python manage.py migrate
python manage.py createsuperuser

# 5. Start the server
python manage.py runserver
```

- Admin: http://127.0.0.1:8000/admin/
- API root: http://127.0.0.1:8000/api/

## API endpoints

| Ticket | Method | URL | Body |
| --- | --- | --- | --- |
| HRMS-113 | POST | `/api/departments/` | `{"name": "Engineering", "description": "..."}` |
| HRMS-114 | POST | `/api/job-positions/` | `{"department": 1, "title": "Backend Developer", "description": "...", "required_skills": ["Python", "Django"]}` |
| HRMS-115 | POST | `/api/candidates/` | `{"full_name": "Sara Ali", "email": "sara@example.com", "phone": "+962 79 000 0000"}` |
| HRMS-116 | POST | `/api/resumes/` | multipart form: `candidate=1`, `file=@resume.pdf` |
| HRMS-117 | GET | `/api/screening-results/<id>/` | none |
| HRMS-118 | GET | `/api/interview-question-sets/<id>/` | none |

Screening results and interview question sets are read-only through the API.
Create test records for them in the admin.

## Validation rules

- **Department:** name is required and unique (case-insensitive).
- **Job position:** department must exist; title is required; `required_skills` must be a list of
  non-empty strings (duplicates are removed).
- **Candidate:** full name is required; email must be valid and unique (case-insensitive, stored
  lowercase); phone is optional but must look like a phone number.
- **Resume:** candidate must exist; file must be `.pdf`, `.docx` or `.txt`, not empty, at most 5 MB.
- **Screening result:** score must be between 0 and 100; recommendation is `proceed`, `hold` or `reject`.
- Invalid input returns `400` with field errors; a missing record returns `404`.

## Example requests

```bash
curl -X POST http://127.0.0.1:8000/api/departments/ \
  -H "Content-Type: application/json" \
  -d '{"name": "Engineering"}'

curl -X POST http://127.0.0.1:8000/api/resumes/ \
  -F candidate=1 -F file=@resume.pdf
```
