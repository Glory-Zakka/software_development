# Nascomsoft Course Registration — Classroom Demo

A beginner FastAPI project with a small server-rendered HTML/CSS dashboard.

## Quick start

1. Create a virtual environment: `python -m venv .venv` (use `python3` where needed).
2. Activate it: Windows PowerShell `.venv\Scripts\Activate.ps1`; macOS/Linux `source .venv/bin/activate`.
3. Install dependencies: `python -m pip install -r requirements.txt`.
4. Run: `python -m uvicorn main:app --reload`.
5. Open `http://127.0.0.1:8000/` and `http://127.0.0.1:8000/docs`.

## What you can do

- List training courses and view one course.
- Create, read, update, delete and filter enrollment records.
- Register students and manage enrollments in a simple HTML interface.
- Try the REST API through FastAPI's `/docs` page.

## Deployment note

A Python host such as Render can run the app from a GitHub repo. Build: `pip install -r requirements.txt`. Start: `uvicorn main:app --host 0.0.0.0 --port $PORT`.

## Important limitations

This is an educational prototype. It has no authentication, no permanent storage, and very basic email checking. **Do not enter real students' personal information**. All enrollment data disappears when the app process restarts or is redeployed.
