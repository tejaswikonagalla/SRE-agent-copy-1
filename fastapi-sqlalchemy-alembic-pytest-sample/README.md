# FastAPI, SQLAlchemy, Alembic, and Pytest Sample

This repository provides a sample setup for a FastAPI application using SQLAlchemy for ORM, Alembic for migrations, and Pytest for testing.

## Project Structure

```
repo/
│
├── app/
│   ├── __init__.py
│   ├── main.py
│   ├── models.py
│   ├── crud.py
│   ├── database.py
│   └── schemas.py
│
├── alembic/
│   ├── env.py
│   ├── README
│   ├── script.py.mako
│   └── versions/
│
├── tests/
│   ├── __init__.py
│   ├── test_main.py
│   └── test_crud.py
│
├── alembic.ini
├── requirements.txt
└── README.md
```

## Setup Instructions

1. **Clone the repository:**

   ```bash
   git clone <repository-url>
   cd fastapi-sqlalchemy-alembic-pytest-sample
   ```

2. **Create and activate a virtual environment:**

   ```bash
   python -m venv venv
   source venv/bin/activate  # On Windows use `venv\Scripts\activate`
   ```

3. **Install dependencies:**

   ```bash
   pip install -r requirements.txt
   ```

4. **Run database migrations:**

   ```bash
   alembic upgrade head
   ```

5. **Start the FastAPI application:**

   ```bash
   uvicorn app.main:app --reload
   ```

6. **Run tests:**

   ```bash
   pytest
   ```

## Common Issues

- **Migration failed**: Ensure your database is properly configured in `app/database.py`. Check the `alembic/env.py` file for correct database connection settings and ensure the `versions` directory is not empty or missing migration scripts.

- **ModuleNotFoundError**: Ensure all modules are correctly referenced in the imports. Check the `app` directory for missing `__init__.py` files or incorrect import paths. Ensure all dependencies in `requirements.txt` are installed.

## Additional Notes

- Ensure your database is properly configured in `app/database.py`.
- Update `alembic.ini` with your database connection details if necessary.