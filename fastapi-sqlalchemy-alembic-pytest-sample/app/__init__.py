# Marks the app directory as a Python package.

# Import necessary modules to ensure they are recognized as part of the package
from .main import app

# Import the models and database to ensure they are included in migrations
from . import models
from .database import Base, engine

# Create all tables in the database. This is usually done by Alembic migrations,
# but for the sake of ensuring the database is in sync, we include this here.
Base.metadata.create_all(bind=engine)