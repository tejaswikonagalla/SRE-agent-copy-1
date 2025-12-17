from typing import Generator
from sqlalchemy.orm import Session
from app.database import SessionLocal

def get_database() -> Generator[Session, None, None]:
    db = SessionLocal()
    try:
        yield db
    except Exception as e:
        db.rollback()
        raise
    finally:
        db.close()  # Ensure the session is closed